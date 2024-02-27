import React, { useCallback } from 'react';
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
import dayjs from 'dayjs';
import { useApi } from '../../hooks';
import { gather } from '../../store';
import TableLayout from '../../components/tableLayout';
import { date } from '../../utils';
import { SearchResponseData } from '../../api/tk/type';
import styles from './index.module.scss';
import type { RenderParams } from '../../components/tableLayout';

const { useGather } = gather;
const { disableNowDate, defaultDateFormat } = date;

const Gather: React.FC = () => {
  const { tk } = useApi();
  const [form] = Form.useForm();
  const searchFormData = useGather();
  const [loading, setLoading] = React.useState(false);
  const [dataSource, setDataSource] = React.useState<SearchResponseData>([]);

  const handleSearch = useLockFn(async () => {
    try {
      setLoading(true);
      await form.validateFields();
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

  const handleDownload = (value: string) => {
    window.open(value);
  };

  const columns: TableProps['columns'] = [
    {
      title: '封面',
      render: value => {
        return <Image className={styles.cover} src={value} />;
      },
      dataIndex: 'dynamic_cover',
    },
    {
      title: '音乐地址',
      render: value => {
        return <audio src={value} controls></audio>;
      },
      dataIndex: 'music_url',
    },
    {
      title: '描述',
      dataIndex: 'desc',
    },
    { title: '类型', dataIndex: 'type' },
    {
      title: '操作',
      dataIndex: 'downloads',
      render: value => {
        return (
          <Button
            type="primary"
            onClick={() => {
              handleDownload(value);
            }}
          >
            查看
          </Button>
        );
      },
    },
  ];

  // 因为react会比较type，如果不缓存一下，那每次的type为FunctionComponent都会不同
  const table = useCallback(
    (props: RenderParams) => {
      const { height } = props;

      if (!height) return null;

      return (
        <Table
          sticky
          bordered
          columns={columns}
          rowKey="dynamic_cover"
          dataSource={dataSource}
          scroll={{ y: height - 120 }}
        />
      );
    },
    [dataSource],
  );

  return (
    <div className={styles.container}>
      <Form
        form={form}
        initialValues={{
          ...searchFormData,
          publish_time: dayjs(searchFormData.publish_time),
        }}
        onValuesChange={handleValueChanges}
      >
        <Flex wrap="wrap" gap="large">
          <Form.Item
            label="关键字"
            name="keyword"
            required
            rules={[{ type: 'string', required: true }]}
          >
            <Input />
          </Form.Item>

          <Form.Item label="发布时间" name="publish_time">
            <DatePicker
              format={defaultDateFormat}
              disabledDate={disableNowDate}
            />
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

      <TableLayout>{table}</TableLayout>
    </div>
  );
};

export default Gather;
