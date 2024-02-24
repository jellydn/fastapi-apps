/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { app__routers__items__ResponseMessage } from '../models/app__routers__items__ResponseMessage';
import type { Item } from '../models/Item';
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
            url: '/items',
        });
    }
    /**
     * Create Item
     * @returns app__routers__items__ResponseMessage Successful Response
     * @throws ApiError
     */
    public createItemItemsPost(): CancelablePromise<app__routers__items__ResponseMessage> {
        return this.httpRequest.request({
            method: 'POST',
            url: '/items',
        });
    }
}
