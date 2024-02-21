import './App.css';
import React from 'react';
import { useRoutes } from 'react-router-dom';
import Layout from './pages/layout';
import Params from './pages/params';
import Gather from './pages/gather';
import Download from './pages/download';
import Process from './pages/process';

const App: React.FC = () => {
  const element = useRoutes([
    {
      path: '/',
      element: <Layout />,
      children: [
        {
          path: 'params',
          index: true,
          element: <Params />,
        },
        { path: 'gather', element: <Gather /> },
        { path: 'download', element: <Download /> },
        { path: 'process', element: <Process /> },
      ],
    },
  ]);

  return element;
};

export default App;
