// apps/client/generated/FastApiDemoClient.test.ts

import { FastApiDemoClient } from './FastApiDemoClient';

describe('FastApiDemoClient', () => {
  let client: FastApiDemoClient;

  beforeEach(() => {
    // Mock configuration
    const config = {
      BASE: 'https://example.com',
      VERSION: '1.0.0',
      WITH_CREDENTIALS: true,
      CREDENTIALS: 'include',
      TOKEN: 'token',
      USERNAME: 'username',
      PASSWORD: 'password',
      HEADERS: { 'Content-Type': 'application/json' },
      ENCODE_PATH: true,
    };

    // Create a new instance of FastApiDemoClient
    client = new FastApiDemoClient(config);
  });

  it('should initialize FastApiDemoClient with the provided configuration', () => {
    expect(client.request.BASE).toBe('https://example.com');
    expect(client.request.VERSION).toBe('1.0.0');
    expect(client.request.WITH_CREDENTIALS).toBe(true);
    expect(client.request.CREDENTIALS).toBe('include');
    expect(client.request.TOKEN).toBe('token');
    expect(client.request.USERNAME).toBe('username');
    expect(client.request.PASSWORD).toBe('password');
    expect(client.request.HEADERS).toEqual({ 'Content-Type': 'application/json' });
    expect(client.request.ENCODE_PATH).toBe(true);
  });

  it('should have items, root, and users properties', () => {
    expect(client.items).toBeDefined();
    expect(client.root).toBeDefined();
    expect(client.users).toBeDefined();
  });

  it('should have request property of type BaseHttpRequest', () => {
    expect(client.request).toBeInstanceOf(BaseHttpRequest);
  });
});
