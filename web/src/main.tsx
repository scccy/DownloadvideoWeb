import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import zhCN from 'antd/locale/zh_CN';
import { ConfigProvider } from 'antd';
import App from './App.tsx';
import { ApiContext, apiInstance } from './api/instance.ts';

ReactDOM.createRoot(document.querySelector('#root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <ApiContext.Provider value={apiInstance}>
        <ConfigProvider locale={zhCN}>
          <App />
        </ConfigProvider>
      </ApiContext.Provider>
    </BrowserRouter>
  </React.StrictMode>,
);
