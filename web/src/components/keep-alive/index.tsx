import { useUnmount } from 'ahooks';
import React from 'react';
import { useLocation, useMatch } from 'react-router-dom';

type KeepAliveProps = {
  children: React.ReactElement;
};

const KeepAlive: React.FC<KeepAliveProps> = props => {
  const { children } = props;
  const location = useLocation();
  const match = useMatch(location.pathname);
  const cache = React.useRef(new Map<string | null, React.ReactElement>());
  cache.current.set(location.pathname, children);

  const keepAliveArray = [...cache.current].map(value => {
    const [pathName, reactElement] = value;

    if (pathName === match?.pathname) return reactElement;

    return (
      <div key={reactElement.key} style={{ display: 'none' }}>
        {reactElement}
      </div>
    );
  });

  return <>{keepAliveArray}</>;
};

export default KeepAlive;
