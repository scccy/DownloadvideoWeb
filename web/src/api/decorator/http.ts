import axios, { AxiosInstance } from 'axios';

type Request = (config: Parameters<AxiosInstance['request']>[0]) => {
  abort: AbortController['abort'];
  request: ReturnType<AxiosInstance['request']>;
};

function http(path: string) {
  const axiosInstance = axios.create({
    baseURL: path,
  });

  const request = (config: Parameters<typeof axiosInstance.request>[0]) => {
    const abortController = new AbortController();
    axiosInstance.request({ ...config, signal: abortController.signal });

    return {
      request,
      abort: abortController.abort,
    };
  };

  return function (constructor: new (...args: any[]) => any) {
    return class extends constructor {
      request = request;
    } as any;
  };
}

export { http };
export type { Request };
