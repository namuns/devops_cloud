function TopNav({ changePageName }) {
  return (
    <ul>
      <li>
        <a onClick={() => changePageName('about')}>About</a>
      </li>
      <li>
        <a onClick={() => changePageName('counter')}>Counter</a>
      </li>
    </ul>
  );
}

export default TopNav;
