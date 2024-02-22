import { describe, it, expect, jest } from '@jest/globals';
import { HttpHandler, createHttpHandler } from '../src/httpHandler';

describe("api base url setup", () => {
  jest.mock("../src/httpHandler", () => {
    return {
      HttpHandler: jest.fn().mockImplementation(() => {
        return {
          post: jest.fn().mockResolvedValue({}),
        };
      }),
    };
  });
  // const mockedCreateHttpHandler = createHttpHandler as jest.MockedFunction<typeof createHttpHandler>;
  const mockHandler = jest.spyOn(HttpHandler.prototype, "baseUrl").mockImplementation((...args) => {
    return new HttpHandler(args[0] as string, args[1] as { [key: string]: string; });
  });

  it("should use baseUrl from configuration", () => {
    const _ = createHttpHandler("argument.api", undefined, {});
    // console.log(mockedHttpHandler.mock.calls);
    expect(mockHandler).toHaveBeenCalledWith("argument.api", expect.any(Object));
    // console.log(mockedCreateHttpHandler);
  });
});
