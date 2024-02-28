import { Flex, Form, Input, InputNumber, Switch, Tooltip } from 'antd';
import React from 'react';
import { QuestionCircleTwoTone } from '@ant-design/icons';
import styles from './index..module.scss';

const Params: React.FC = () => {
  return (
    <Form layout="vertical" className={styles.container}>
      <Flex
        vertical
        align="flex-start"
        wrap="wrap"
        className={styles.flexContainer}
      >
        <Form.Item name="root" label="下载路径">
          <Input />
        </Form.Item>

        <Form.Item name="folder_name" label="下载文件夹">
          <Input />
        </Form.Item>

        <Form.Item name="name_format" label="文件保存时的命名规则">
          <Input
            suffix={
              <Tooltip
                title="文件保存时的命名规则, 值之间使用空格分隔
            默认值: 发布时间-作品类型-账号昵称-描述
            id: 作品 ID, desc: 作品描述, create_time: 发布时间
            nickname: 账号昵称, mark: 账号标识, uid: 账号 ID, type: 作品类型"
              >
                <QuestionCircleTwoTone />
              </Tooltip>
            }
          />
        </Form.Item>

        <Form.Item name="date_format" label="日期时间格式">
          <Input />
        </Form.Item>

        <Form.Item name="split" label="文件命名的分隔符">
          <Input />
        </Form.Item>

        <Form.Item
          name="folder_mode"
          label="是否将每个作品的文件储存至单独的文件夹"
        >
          <Switch />
          <Tooltip title="是否将每个作品的文件储存至单独的文件夹，文件夹名称格式与 name_format 参数保持一致，默认值: false">
            <QuestionCircleTwoTone />
          </Tooltip>
        </Form.Item>

        <Form.Item name="music" label="是否下载作品音乐">
          <Switch />
        </Form.Item>

        <Form.Item name="storage_format" label="采集数据持久化储存格式">
          <Input
            suffix={
              <Tooltip
                title="采集数据持久化储存格式, 设置为空字符串代表不保存
              支持: csv、xlsx、sql(SQLite)"
              >
                <QuestionCircleTwoTone />
              </Tooltip>
            }
          />
        </Form.Item>

        <Form.Item name="cookie" label="抖音网页版 Cookie">
          <Input.TextArea />
          <Tooltip title="抖音网页版 Cookie, 必需参数; 建议通过程序写入配置文件，亦可手动编辑">
            <QuestionCircleTwoTone />
          </Tooltip>
        </Form.Item>

        <Form.Item name="dynamic_cover" label="是否下载动态封面图">
          <Switch />
        </Form.Item>

        <Form.Item name="original_cover" label="是否下载静态封面图">
          <Switch />
        </Form.Item>

        <Form.Item name="max_size" label="作品文件大小限制">
          <InputNumber
            suffix={
              <Tooltip title="作品文件大小限制, 单位字节, 超出大小限制的作品文件将会跳过下载设置为 0 代表无限制">
                <QuestionCircleTwoTone />
              </Tooltip>
            }
          />
        </Form.Item>

        <Form.Item name="chunk" label="作品文件大小限制">
          <InputNumber
            suffix={
              <Tooltip title="每次从服务器接收的数据块大小, 单位字节; 默认值：1048576(1 MB)">
                <QuestionCircleTwoTone />
              </Tooltip>
            }
          />
        </Form.Item>

        <Form.Item
          name="chunk"
          label="发送请求获取数据发生异常时重试的最大次数"
        >
          <InputNumber
            suffix={
              <Tooltip title="每次从服务器接收的数据块大小, 单位字节; 默认值：1048576(1 MB)">
                <QuestionCircleTwoTone />
              </Tooltip>
            }
          />
        </Form.Item>

        <Form.Item name="max_pages" label="下载最大次数">
          <InputNumber
            suffix={
              <Tooltip title="每次从服务器接收的数据块大小, 单位字节; 默认值：1048576(1 MB)">
                <QuestionCircleTwoTone />
              </Tooltip>
            }
          />
        </Form.Item>
      </Flex>
    </Form>
  );
};

export default Params;
