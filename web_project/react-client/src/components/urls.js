export const urls = [
  { title: 'Home', path: '/' },
  // { title: 'About', path: '/about' },
  // { title: 'Analysis', path: '/analysis' },
  { title: 'News', path: '/news' }
];

export const createNewsPath = (newsTitle) => `/news/${newsTitle}`;