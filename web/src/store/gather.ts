import { create } from 'zustand';
import { persist } from 'zustand/middleware';

type Value = {
  type: string;
  pages: string;
  keyword: string;
  sort_type: string;
  publish_time: string;

  setParams: (prams: Omit<Value, 'setParams'>) => void;
};

const useGather = create(
  persist<Value>(
    set => ({
      type: '',
      pages: '',
      keyword: '',
      sort_type: '',
      publish_time: '',

      setParams(value) {
        set(value);
      },
    }),
    {
      name: 'params',
    },
  ),
);

export { useGather };
