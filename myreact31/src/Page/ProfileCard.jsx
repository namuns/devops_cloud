import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars, faStickyNote } from "@fortawesome/free-solid-svg-icons";

function ProfileCard({
  memberNo,
  name,
  role,
  facebook_url,
  email,
  className,
  children,
}) {
  return (
    <div className={className}>
      <h2>Profile Card</h2>
      <>
        <section>
          <nav className="menu">
            <a href="#">
              <FontAwesomeIcon icon={faBars} />
            </a>
            <a href="#">
              <FontAwesomeIcon icon={faStickyNote} />
            </a>
          </nav>
          <article className="profile">
            <img src={`/profile-images/${memberNo}.jpg`} alt="프로필 이미지" />
            <h1>{name}</h1>
            <h2>{role}</h2>
            <a href="#" className="btnView">
              VIEW MORE
            </a>
          </article>
          <ul className="contact">
            <li>
              <i className="fab fa-facebook-f" />
              <span>{facebook_url}</span>
            </li>
            <li>
              <i className="fas fa-envelope" />
              <span>{email}</span>
            </li>
          </ul>
          <nav className="others">{children}</nav>
        </section>
      </>
    </div>
  );
}

export default ProfileCard;
