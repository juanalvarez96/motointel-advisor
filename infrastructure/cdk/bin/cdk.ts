#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { MotoIntelAdvisorStack } from '../lib/motointel-advisor-stack';

const app = new cdk.App();

new MotoIntelAdvisorStack(app, 'MotoIntelAdvisorDevStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION ?? 'eu-west-1',
  },
});