/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Item } from '../models/Item';
import type { ResponseMessage } from '../models/ResponseMessage';
import type { CancelablePromise } from '../core/CancelablePromise';
import type { BaseHttpRequest } from '../core/BaseHttpRequest';
export class ItemsService {
    constructor(public readonly httpRequest: BaseHttpRequest) {}
    /**
     * Get Items
     * @returns Item Successful Response
     * @throws ApiError
     */
    public getItemsItemsGet(): CancelablePromise<Array<Item>> {
        return this.httpRequest.request({
            method: 'GET',
            url: '/items/',
        });
    }
    /**
     * Create Item
     * @returns ResponseMessage Successful Response
     * @throws ApiError
     */
    public createItemItemsPost(): CancelablePromise<ResponseMessage> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/items/',
        });
    }
}
