// import { describe, it, expect, vi } from 'vitest';
// import { HttpHandler, createHttpHandler } from '../src/httpHandler';

// describe("api base url setup", () => {
//   vi.mock("../src/httpHandler", () => {
//     return {
//       HttpHandler: vi.fn().mockImplementation(() => {
//         return {
//           post: vi.fn().mockResolvedValue({}),
//         };
//       }),
//     };
//   });
//   // const mockedCreateHttpHandler = createHttpHandler as vi.MockedFunction<typeof createHttpHandler>;
//   const mockHandler = vi.spyOn(HttpHandler.prototype, "get").mockImplementation((baseUrl: string, headers?: { [key: string]: string; }) => {
//     return new HttpHandler(baseUrl, headers).get;
//   });

//   it("should use baseUrl from configuration", () => {
//     const _ = createHttpHandler("argument.api", undefined, {});
//     // console.log(mockedHttpHandler.mock.calls);
//     expect(mockHandler).toHaveBeenCalledWith("argument.api", expect.any(Object));
//     // console.log(mockedCreateHttpHandler);
//   });
// });
