import React from 'react';
import { Tk } from './tk';

class ApiInstance {
  tk = new Tk();
}

const apiInstance = new ApiInstance();
const ApiContext = React.createContext<ApiInstance>(apiInstance);

export { ApiInstance, ApiContext, apiInstance };
