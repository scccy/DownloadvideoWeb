import React from 'react';
import {
  Button,
  DatePicker,
  Flex,
  Form,
  FormProps,
  Image,
  Input,
  Switch,
  Table,
  TableProps,
} from 'antd';
import { useLockFn } from 'ahooks';
import { useApi } from '../../hooks';
import { useGather } from '../../store/gather';
import TableLayout from '../../components/tableLayout';
import { date } from '../../utils';
import styles from './index.module.scss';

const { defaultDateFormat } = date;

const Gather: React.FC = () => {
  const { tk } = useApi();
  const searchFormData = useGather();
  const [loading, setLoading] = React.useState(false);
  const [dataSource, setDataSource] = React.useState([]);

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

      setDataSource(result.data);
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

  const columns: TableProps['columns'] = [
    {
      title: '封面',
      render: value => {
        return <Image className={styles.cover} src={value} />;
      },
      dataIndex: 'dynamic_cover',
      key: 'dynamic_cover',
    },
    {
      title: '音乐地址',
      render: value => {
        return <audio src={value} controls></audio>;
      },
      dataIndex: 'music_url',
      key: 'music_url',
    },
    {
      title: '描述',
      dataIndex: 'desc',
      key: 'desc',
    },
  ];

  return (
    <div className={styles.container}>
      <Form onValuesChange={handleValueChanges}>
        <Flex wrap="wrap" gap="large" defaultValue={searchFormData}>
          <Form.Item label="关键字" name="keyword" required>
            <Input />
          </Form.Item>

          <Form.Item label="搜索类型" name="type">
            <Input />
          </Form.Item>

          <Form.Item label="搜索页数" name="pages">
            <Input type="number" />
          </Form.Item>

          <Form.Item label="排序依据" name="sort_type">
            <Input />
          </Form.Item>

          <Form.Item label="发布时间" name="publish_time">
            <DatePicker format={defaultDateFormat} />
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

      <TableLayout>
        {props => {
          const { height } = props;

          if (!height) return null;

          return (
            <Table
              rowKey={'dynamic_cover'}
              sticky
              bordered
              columns={columns}
              dataSource={dataSource}
              scroll={{ y: height - 170 }}
            />
          );
        }}
      </TableLayout>
    </div>
  );
};

export default Gather;
