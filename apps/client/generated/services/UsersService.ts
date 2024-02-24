/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { app__routers__users__ResponseMessage } from '../models/app__routers__users__ResponseMessage';
import type { CancelablePromise } from '../core/CancelablePromise';
import type { BaseHttpRequest } from '../core/BaseHttpRequest';
export class UsersService {
    constructor(public readonly httpRequest: BaseHttpRequest) {}
    /**
     * Create User
     * @returns app__routers__users__ResponseMessage Successful Response
     * @throws ApiError
     */
    public createUserUsersPost(): CancelablePromise<app__routers__users__ResponseMessage> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/users',
        });
    }
}
