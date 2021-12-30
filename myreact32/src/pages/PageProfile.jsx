import { useState, useEffect } from 'react';
import Axios from 'axios';

function PageProfile() {
  const [profileList, setProfileList] = useState([]);
  const [profileData, setProfileData] = useState([]);
  const [error, setError] = useState(null);
  const [query, setQuery] = useState('');

  useEffect(() => {
    // handleRefresh();
    setProfileList(profileData);
  }, [profileData]);

  const handleRefresh = () => {
    setError(null);
    Axios.get(
      'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
    )
      .then((response) => {
        const axiosProfileList = response.data.map((bts) => ({
          role: bts.role,
          mbti: bts.mbti,
          name: bts.name,
          uniqueId: bts.unique_id,
          profileImageUrl: bts.profile_image_url,
          instagramUrl: bts.instagram_url,
        }));
        setProfileData(axiosProfileList);
      })
      .catch((error) => {
        console.error(error);
        setError(error);
      });
  };

  const clearProfile = () => {
    setProfileList([]);
  };

  const handleChange = (e) => {
    const value = e.target.value;
    console.log(value);
    setQuery(value);
  };
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      query &&
        setProfileList(
          profileData.filter((profile) => {
            const data = Object.values(profile);
            let state = '';
            for (const info of data) {
              if (info.includes(query)) {
                state = 'true';
              }
            }
            return state === 'true' ? true : false;
          }),
        );
    }
  };
  return (
    <div>
      <button onClick={clearProfile}>Clear</button>
      <button onClick={handleRefresh}>Refresh</button>
      {profileList.length === 0 && <h3>등록된 프로필이 없습니다.</h3>}
      {error !== null && (
        <h3>조회 시에 오류가 발생했습니다. 잠시 후 다시 시도해주세요.</h3>
      )}
      <input
        type="text"
        placeholder="검색어를 입력해주세요."
        onChange={handleChange}
        onKeyPress={handleKeyPress}
      />
      {profileList.map((bts) => {
        return (
          <div key={bts.uniqueId}>
            <ul>
              <img src={bts.profileImageUrl} alt="프로필 이미지" />
              <h3>{bts.name}</h3>
              <li>{bts.uniqueId}</li>
              <li>{bts.role}</li>
              <li>{bts.mbti}</li>
              <li>{bts.instagramUrl}</li>
            </ul>
          </div>
        );
      })}
    </div>
  );
}

export default PageProfile;
