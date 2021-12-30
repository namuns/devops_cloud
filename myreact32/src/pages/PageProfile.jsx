import { useState, useEffect } from 'react';
import Axios from 'axios';

function PageProfile() {
  const [profileList, setProfileList] = useState([]);

  useEffect(() => {
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
        setProfileList(axiosProfileList);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      {profileList.length === 0 && <h3>등록된 프로필이 없습니다.</h3>}
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
