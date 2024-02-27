import { create } from 'zustand';
import { persist } from 'zustand/middleware';

type Value = {
  cookie: string;
  setParams: (prams: Omit<Value, 'setParams'>) => void;
};

const useParams = create(
  persist<Value>(
    set => ({
      cookie: '',

      setParams(value) {
        set(value);
      },
    }),
    {
      name: 'params',
    },
  ),
);

export { useParams };
