/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { HelloMessage } from '../models/HelloMessage';
import type { CancelablePromise } from '../core/CancelablePromise';
import type { BaseHttpRequest } from '../core/BaseHttpRequest';
export class RootService {
    constructor(public readonly httpRequest: BaseHttpRequest) {}
    /**
     * Read Root
     * @returns HelloMessage Successful Response
     * @throws ApiError
     */
    public readRootGet(): CancelablePromise<HelloMessage> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/',
        });
    }
}
