import React from 'react';
import { useUpdate } from 'ahooks';
import styles from './index.module.scss';

type RenderParams = {
  height: number;
};

type TableLayoutProps = {
  children: React.FC<RenderParams>;
};

const TableLayout: React.FC<TableLayoutProps> = props => {
  const { children } = props;
  const [height, setHeight] = React.useState(0);
  const container = React.useRef<HTMLElement>();

  const resizeFn = React.useRef(() => {
    if (!container.current) return;

    setHeight(container.current.offsetHeight);
  });

  const table = React.createElement(children, {
    height,
  });

  React.useEffect(() => {
    resizeFn.current();
    window.addEventListener('resize', resizeFn.current);
    return () => {
      window.removeEventListener('resize', resizeFn.current);
    };
  }, []);

  React.useEffect(() => {
    resizeFn.current();
  }, [container]);

  return (
    <div
      className={styles.container}
      ref={ref => {
        if (!ref) return;
        container.current = ref;
      }}
    >
      {table}
    </div>
  );
};

export default TableLayout;
export type { RenderParams };
