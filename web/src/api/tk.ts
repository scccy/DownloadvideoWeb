import { AxiosInstance } from 'axios';
import { http } from './decorator';

@http('tk')
class Tk {
  http: AxiosInstance | null = null;

  search() {
    this.http?.post('search');
  }
}

export { Tk };
