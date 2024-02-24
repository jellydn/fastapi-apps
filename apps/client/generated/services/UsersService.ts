/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ResponseMessage } from '../models/ResponseMessage';
import type { CancelablePromise } from '../core/CancelablePromise';
import type { BaseHttpRequest } from '../core/BaseHttpRequest';
export class UsersService {
    constructor(public readonly httpRequest: BaseHttpRequest) {}
    /**
     * Create User
     * @returns ResponseMessage Successful Response
     * @throws ApiError
     */
    public createUserUsersPost(): CancelablePromise<ResponseMessage> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/users/',
        });
    }
}
