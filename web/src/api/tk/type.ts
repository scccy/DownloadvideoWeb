type SearchData = {
  keyword: string;
  type: string;
  pages: string;
  sort_type: string;
  publish_time: string;
};

type SearchResponseData = {
  collect_count: string;
  collection_time: string;
  comment_count: string;
  create_time: string;
  create_timestamp: string;
  desc: string;
  digg_count: string;
  downloads: string;
  duration: string;
  dynamic_cover: string;
  extra: string;
  height: string;
  id: string;
  mark: string;
  music_author: string;
  music_title: string;
  music_url: string;
  nickname: string;
  origin_cover: '';
  ratio: string;
  sec_uid: string;
  share_count: string;
  share_url: string;
  short_id: string;
  signature: string;
  tag_1: string;
  tag_2: string;
  tag_3: string;
  text_extra: string;
  type: string;
  uid: string;
  unique_id: string;
  uri: string;
  user_age: string;
  width: number;
}[];

type SettingData = {
  root: string;
  folder_name: string;
  name_format: string;
  date_format: string;
  split: string;
  folder_mode: string;
  music: string;
  storage_format: string;
  cookie: string;
  dynamic_cover: string;
  original_cover: string;
  proxies: string;
  download: string;
  max_size: string;
  chunk: string;
  max_retry: string;
  max_pages: string;
  default_mode: string;
  ffmpeg: string;
  token: string;
};

type SettingResponseData = {
  root: string;
  folder_name: string;
  name_format: string;
  date_format: string;
  split: string;
  folder_mode: string;
  music: string;
  storage_format: string;
  cookie: string;
  dynamic_cover: string;
  original_cover: string;
  proxies: string;
  download: string;
  max_size: string;
  chunk: string;
  max_retry: string;
  max_pages: string;
  default_mode: string;
  ffmpeg: string;
  token: string;
};

export type {
  SearchData,
  SearchResponseData,
  SettingData,
  SettingResponseData,
};
