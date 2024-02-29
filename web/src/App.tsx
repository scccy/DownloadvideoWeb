import './App.css';
import React from 'react';
import { redirect, useMatch, useRoutes } from 'react-router-dom';
import Layout from './pages/layout';
import Params from './pages/params';
import Gather from './pages/gather';
import Download from './pages/download';
import Process from './pages/process';

const App: React.FC = () => {
  const element = useRoutes([
    {
      path: '/',
      loader: () => {
        redirect('/params');
        return null;
      },
      element: <Layout />,
      children: [
        {
          path: 'params',
          element: <Params key="params" />,
        },
        { path: 'gather', element: <Gather key="gather" /> },
        { path: 'download', element: <Download key="download" /> },
        { path: 'process', element: <Process key="process" /> },
      ],
    },
  ]);

  return element;
};

export default App;
