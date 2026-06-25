import * as cdk from 'aws-cdk-lib';
import { CfnOutput, RemovalPolicy, Stack, StackProps, Tags } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as s3 from 'aws-cdk-lib/aws-s3';

export class MotoIntelAdvisorStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const projectName = 'motointel-advisor';
    const environment = 'dev';

    Tags.of(this).add('Project', projectName);
    Tags.of(this).add('Environment', environment);
    Tags.of(this).add('ManagedBy', 'aws-cdk');

    const dataBucket = new s3.Bucket(this, 'DataBucket', {
      bucketName: `${projectName}-${environment}-data-${this.account}-${this.region}`,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      encryption: s3.BucketEncryption.S3_MANAGED,
      enforceSSL: true,
      versioned: true,
      removalPolicy: RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    const knowledgeTable = new dynamodb.Table(this, 'KnowledgeTable', {
      tableName: `${projectName}-${environment}-knowledge`,
      partitionKey: {
        name: 'pk',
        type: dynamodb.AttributeType.STRING,
      },
      sortKey: {
        name: 'sk',
        type: dynamodb.AttributeType.STRING,
      },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY,
    });

    new CfnOutput(this, 'DataBucketName', {
      value: dataBucket.bucketName,
      description: 'S3 bucket for MotoIntel Advisor data',
    });

    new CfnOutput(this, 'KnowledgeTableName', {
      value: knowledgeTable.tableName,
      description: 'DynamoDB table for structured motorcycle knowledge',
    });
  }
}