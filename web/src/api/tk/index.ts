import { http } from '../decorator';
import type { Request } from '../decorator/http';
import type { SearchData, SearchResponseData } from './type';

@http('tk')
class Tk {
  request: Request;

  /**
   * 搜索·
   * @param {SearchParams} params
   */
  search(data: SearchData) {
    return this.request<SearchResponseData>({
      url: 'search',
      method: 'post',
      data,
    });
  }
}

export { Tk };
