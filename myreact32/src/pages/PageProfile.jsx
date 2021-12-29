import { useState } from 'react';

function PageProfile() {
  const [profileList, setProfileList] = useState([
    {
      uniqueId: 'bts-jin',
      name: '진',
      role: '서브보컬',
      mbti: 'INFP',
      instagramUrl: 'https://instagram.com/jin',
      profileImageUrl:
        'https://classdevopscloud.blob.core.windows.net/data/bts-jin.jpg',
    },
  ]);

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
