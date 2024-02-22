import React from 'react';
import {
  Button,
  DatePicker,
  Flex,
  Form,
  FormProps,
  Input,
  Switch,
  Table,
} from 'antd';
import { useLockFn } from 'ahooks';
import { useApi } from '../../hooks';
import { useGather } from '../../store/gather';
import styles from './index.module.scss';

const Gather: React.FC = () => {
  const { tk } = useApi();
  const searchFormData = useGather();
  const [loading, setLoading] = React.useState(false);

  const handleSearch = useLockFn(async () => {
    setLoading(true);
    try {
      const { keyword, type, pages, sort_type, publish_time } = searchFormData;
      const { request } = tk.search({
        keyword,
        type,
        pages,
        sort_type,
        publish_time,
      });

      const result = await request;
    } finally {
      setLoading(false);
    }
  });

  const handleValueChanges: FormProps['onValuesChange'] = (
    changeValues,
    values,
  ) => {
    searchFormData.setParams(values);
  };

  return (
    <div className={styles.container}>
      <Form onValuesChange={handleValueChanges}>
        <Flex wrap="wrap" gap="large">
          <Form.Item label="关键字" name="关键字" required>
            <Input />
          </Form.Item>

          <Form.Item label="搜索类型" name="type">
            <Input />
          </Form.Item>

          <Form.Item label="搜索页数" name="pages">
            <Input type="number" defaultValue={1} />
          </Form.Item>

          <Form.Item label="排序依据" name="pages">
            <Input />
          </Form.Item>

          <Form.Item label="发布时间" name="publish_time">
            <DatePicker />
          </Form.Item>

          <Form.Item label="抖音 cookie" name="cookie">
            <Input />
          </Form.Item>

          <Form.Item label="自定义参数" name="token">
            <Input />
          </Form.Item>

          <Form.Item label="是否返回原始数据" name="source">
            <Switch />
          </Form.Item>

          <Form.Item>
            <Button loading={loading} type="primary" onClick={handleSearch}>
              搜索
            </Button>
          </Form.Item>
        </Flex>
      </Form>

      <Table></Table>
    </div>
  );
};

export default Gather;
