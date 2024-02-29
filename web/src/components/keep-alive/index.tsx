import React from 'react';
import { useLocation, useMatch } from 'react-router-dom';
import styles from './index.module.scss';

type KeepAliveProps = {
  children: React.ReactElement;
};

const KeepAlive: React.FC<KeepAliveProps> = props => {
  const { children } = props;
  const location = useLocation();
  const match = useMatch(location.pathname);
  const cache = React.useRef(new Map<string | null, React.ReactElement>());

  if (children.key) cache.current.set(location.pathname, children);

  const keepAliveArray = [...cache.current].map(value => {
    const [pathName, reactElement] = value;

    if (pathName === match?.pathname)
      return (
        <div key={reactElement.key} className={styles.showContainer}>
          {reactElement}
        </div>
      );

    return (
      <div key={reactElement.key} className={styles.hiddenContainer}>
        {reactElement}
      </div>
    );
  });

  return <>{keepAliveArray}</>;
};

export default KeepAlive;
