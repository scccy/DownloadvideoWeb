import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App.tsx';
import { ApiContext, apiInstance } from './api/instance.ts';

ReactDOM.createRoot(document.querySelector('#root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <ApiContext.Provider value={apiInstance}>
        <App />
      </ApiContext.Provider>
    </BrowserRouter>
  </React.StrictMode>,
);
