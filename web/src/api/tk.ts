import { AxiosInstance } from 'axios';

class Tk {
  private http: AxiosInstance!;

  search() {
    this.http.post('/tk/search');
  }
}

export { Tk };
