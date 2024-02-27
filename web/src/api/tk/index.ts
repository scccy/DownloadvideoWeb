import { http } from '../decorator';
import type { Request } from '../decorator/http';
import type {
  SearchData,
  SearchResponseData,
  SettingData,
  SettingResponseData,
} from './type';

@http('tk')
class Tk {
  request: Request;

  /**
   * 搜索·
   * @param {SearchParams} params
   * @returns
   */
  search(data: SearchData) {
    return this.request<SearchResponseData>({
      url: 'search',
      method: 'post',
      data,
    });
  }

  /**
   * 设置
   * @param {SettingData} data
   * @returns
   */
  setting(data: SettingData) {
    return this.request<SettingResponseData>({
      url: 'setting',
      method: 'post',
      data,
    });
  }
}

export { Tk };
