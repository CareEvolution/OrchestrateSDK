import { IHttpHandler } from "./httpHandler.js";

export type BatchResponse<T> = {
  items: T;
};

export async function handleBatchOverload<TIn, TOut>(
  httpHandler: IHttpHandler,
  url: string,
  request: TIn
): Promise<TOut> {
  if (Array.isArray(request)) {
    const batchResponse = await httpHandler.post(`${url}/batch`, { items: request });
    return (batchResponse as BatchResponse<TOut>).items;
  }
  return httpHandler.post(url, request);
}