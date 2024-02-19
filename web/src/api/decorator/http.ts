import axios from 'axios';

function http(path: string) {
  const axiosInstance = axios.create({
    baseURL: path,
  });

  return function (constructor: new (...args: any[]) => any) {
    return class extends constructor {
      http = axiosInstance;
    } as any;
  };
}

export { http };
