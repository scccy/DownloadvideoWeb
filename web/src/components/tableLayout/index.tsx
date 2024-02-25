import React, { useMemo } from 'react';
import styles from './index.module.scss';

type TableLayoutProps = {
  children: React.FC<{
    height: number;
  }>;
};

const TableLayout: React.FC<TableLayoutProps> = props => {
  const { children } = props;
  const [container, setContainer] = React.useState<HTMLElement>();

  const table = React.createElement(children, {
    height: container?.offsetHeight!,
  });

  return (
    <div
      className={styles.container}
      ref={ref => {
        if (!ref) return;
        setContainer(ref);
      }}
    >
      {table}
    </div>
  );
};

export default TableLayout;
