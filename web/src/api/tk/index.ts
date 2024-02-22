import { AxiosInstance } from 'axios';
import { http } from '../decorator';
import type { SearchParams } from './type';

@http('tk')
class Tk {
  request: AxiosInstance | null = null;

  /**
   * 搜索·
   * @param {SearchParams} params
   */
  search(params: SearchParams) {
    this.request?.('search', { method: 'get', params });
  }
}

export { Tk };
