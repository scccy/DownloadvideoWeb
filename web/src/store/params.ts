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

const useParams = create(
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

export { useParams };
