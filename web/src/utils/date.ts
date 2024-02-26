import dayjs from 'dayjs';
import { DatePickerProps } from 'antd';

const defaultDateFormat = 'YYYY/MM/DD';

const disableNowDate: DatePickerProps['disabledDate'] = date => {
  return date.valueOf() >= dayjs().valueOf();
};

export { defaultDateFormat, disableNowDate };
