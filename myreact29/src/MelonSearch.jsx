import { useState } from 'react';
import { Input, List, Avatar, notification, Typography } from 'antd';

import Axios from 'axios';
import jsonpAdaptor from 'axios-jsonp';

function MelonSearch() {
  const [query, setQuery] = useState('');
  const [songList, setSongList] = useState([]);

  const handleChange = (e) => {
    const {
      target: { value },
    } = e;
    console.group('handleChange');
    console.log(value);
    console.groupEnd();
    setQuery(value);
  };
  const handlePressEnter = () => {
    console.group('handlePressEnter');
    console.log('검색어 ${query}(으)로 검색합니다.');
    console.groupEnd();

    const url = 'https://www.melon.com/search/keyword/index.json';

    Axios({
      url: url,
      adapter: jsonpAdaptor,
      callbackParamName: 'jscallback',
      params: {
        query: query,
      },
    })
      .then((response) => {
        //ALBUMCONTENTS, ARTISTCONTENTS 가능
        const {
          data: { SONGCONTENTS: searchedSongList = [] },
        } = response;
        console.group('멜론 검색결과');
        console.log(response);
        console.log(searchedSongList);
        console.groupEnd();

        setSongList(searchedSongList);

        notification.info({
          message: '멜론검색',
          description: `${searchedSongList.length}개의 노래 검색결과가 있습니다.`,
        });
      })
      .catch((error) => {
        console.group('멜론 검색 에러');
        console.error(error);
        console.groupEnd();
        notification.error({
          message: '멜론 검색 에러',
          // 주의: 유저친화적인 에러메세지는 아닙니다.
          description: JSON.stringify(error),
        });
      });
  };

  return (
    <div style={{ width: 300, margin: '0 auto' }}>
      <h2>멜론 검색</h2>
      검색어: {query}
      <Input
        placeholder="검색어를 입력해주세요."
        onChange={handleChange}
        onPressEnter={handlePressEnter}
      />
      <List
        bordered={false}
        dataSource={songList}
        renderItem={(song) => (
          <List.Item>
            <List.Item.Meta avatar={<Avatar src={song.ALBUMIMG} />} />

            <Typography.Text
              onClick={() => {
                console.log(`clicked ${JSON.stringify(song)}`);
              }}
            >
              <a
                href={`https://www.melon.com/song/detail.htm?songId=${song.SONGID}`}
                target={'_blank'}
              >
                {song.SONGNAME}
              </a>
              - {song.ARTISTNAME}
            </Typography.Text>
          </List.Item>
        )}
      />
    </div>
  );
}

export default MelonSearch;
