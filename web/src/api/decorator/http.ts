import { message } from 'antd';
import axios, { AxiosError, AxiosInstance, AxiosResponse } from 'axios';

type Request = <R, T = any>(
  config: Parameters<AxiosInstance['request']>[0],
) => {
  abort: AbortController['abort'];
  request: Promise<AxiosResponse<R, T>>;
};

function http(path: string) {
  const axiosInstance = axios.create({
    baseURL: path,
  });

  axiosInstance.interceptors.response.use(response => {
    return { ...response, data: response.data.data.data };
  });

  const request = (config: Parameters<typeof axiosInstance.request>[0]) => {
    const abortController = new AbortController();
    const request = axiosInstance.request({
      ...config,
      signal: abortController.signal,
    });

    request.catch((e: AxiosError) => {
      message.error(e.message);
    });

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
