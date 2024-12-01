// src/mockdata/news.js

const newsTopics = {
    ai: {
      titles: [
        'AI Breakthrough in Healthcare',
        'Artificial Intelligence Transforms Manufacturing',
        'New AI Model Sets Performance Record',
        'AI Ethics Guidelines Released',
        'Machine Learning Revolution in Finance',
        'AI-Powered Climate Solutions',
        'Neural Networks Make Medical Discovery'
      ],
      summaries: [
        'Revolutionary AI system diagnoses diseases with unprecedented accuracy.',
        'Smart manufacturing systems reduce waste by 50% using AI algorithms.',
        'Latest AI model achieves human-level performance in complex tasks.',
        'Global committee establishes framework for ethical AI development.',
        'AI trading systems transform financial market analysis.',
        'AI technology helps predict and mitigate climate change effects.',
        'Deep learning breakthrough leads to new drug discovery.'
      ]
    },
    tech: {
      titles: [
        'Quantum Computing Milestone',
        '5G Network Expansion',
        'Cybersecurity Breakthrough',
        'New Smartphone Technology',
        'Revolutionary Battery Design',
        'Clean Energy Innovation',
        'Space Technology Advancement'
      ],
      summaries: [
        'Scientists achieve quantum supremacy in groundbreaking experiment.',
        'Next-generation networks reach remote communities.',
        'New encryption method promises unbreakable security.',
        'Revolutionary display technology transforms mobile experience.',
        'New battery design doubles electric vehicle range.',
        'Solar efficiency breakthrough could revolutionize renewable energy.',
        'New propulsion system enables faster space travel.'
      ]
    },
    science: {
      titles: [
        'Medical Research Breakthrough',
        'Climate Study Findings',
        'Space Exploration Discovery',
        'Genetic Engineering Advance',
        'Ocean Conservation Success',
        'Particle Physics Discovery',
        'Renewable Energy Milestone'
      ],
      summaries: [
        'New treatment shows promising results in clinical trials.',
        'Research reveals new patterns in global climate data.',
        'Telescopes capture unprecedented views of distant galaxies.',
        'CRISPR technology achieves new precision in gene editing.',
        'Marine sanctuary shows dramatic recovery in biodiversity.',
        'Large Hadron Collider experiment reveals new particle.',
        'Renewable energy surpasses fossil fuels in major milestone.'
      ]
    },
    health: {
      titles: [
        'Vaccine Development Success',
        'Mental Health Innovation',
        'Nutrition Research Finding',
        'Exercise Science Breakthrough',
        'Healthcare Technology Advance',
        'Wellness Study Results',
        'Medical Device Innovation'
      ],
      summaries: [
        'New vaccine shows 95% efficacy in clinical trials.',
        'Digital therapy platform shows promising mental health outcomes.',
        'Study reveals new benefits of Mediterranean diet.',
        'Research identifies optimal exercise patterns for longevity.',
        'AI-powered diagnostic tool receives FDA approval.',
        'Long-term study reveals keys to healthy aging.',
        'Revolutionary medical device improves patient outcomes.'
      ]
    },
    environment: {
      titles: [
        'Renewable Energy Record',
        'Ocean Cleanup Success',
        'Forest Conservation Victory',
        'Climate Solution Innovation',
        'Wildlife Protection Success',
        'Sustainable City Initiative',
        'Green Technology Breakthrough'
      ],
      summaries: [
        'Solar power achieves new efficiency record.',
        'Innovative system removes 50% more ocean plastic.',
        'Reforestation project exceeds restoration goals.',
        'New carbon capture technology shows promising results.',
        'Endangered species population shows remarkable recovery.',
        'City achieves carbon neutrality ahead of schedule.',
        'Breakthrough in biodegradable materials development.'
      ]
    }
  };
  
  const generateNewsContent = (topic, index) => {
    const topics = Object.keys(newsTopics);
    const selectedTopic = newsTopics[topics[Math.floor(Math.random() * topics.length)]];
    
    return {
      title: selectedTopic.titles[index % selectedTopic.titles.length],
      summary: selectedTopic.summaries[index % selectedTopic.summaries.length],
      content: `${selectedTopic.summaries[index % selectedTopic.summaries.length]} ${Array(5).fill(selectedTopic.summaries[index % selectedTopic.summaries.length]).join(' ')}`,
      image: "https://picsum.photos/800/600"
    };
  };
  
  // Bugünün tarihini al ve UTC'ye çevir
  const getCurrentDate = () => {
    const now = new Date();
    return new Date(Date.UTC(now.getFullYear(), now.getMonth(), now.getDate()));
  };
  
  // Tarihi YYYY-MM-DD formatına çevir
  const formatDate = (date) => {
    return date.toISOString().split('T')[0];
  };
  
  // Son 5 günün tarihlerini oluştur (bugün dahil)
  const generateDates = () => {
    const today = getCurrentDate();
    const dates = [];
    
    for (let i = 4; i >= 0; i--) {
      const date = new Date(today);
      date.setDate(today.getDate() - i);
      dates.push(formatDate(date));
    }
    
    return dates;
  };
  
  // Tarihleri oluştur
  const dates = generateDates();
  console.log('Generated dates:', dates);
  
  // Mock data'yı oluştur
  export const mockNewsData = dates.reduce((acc, date) => {
    // Her gün için 7 haber oluştur
    acc[date] = Array.from({ length: 7 }, (_, index) => {
      const newsContent = generateNewsContent(
        Object.keys(newsTopics)[index % Object.keys(newsTopics).length],
        index
      );
      
      // Haber için rastgele saat oluştur
      const hour = String(Math.floor(Math.random() * 24)).padStart(2, '0');
      const minute = String(Math.floor(Math.random() * 60)).padStart(2, '0');
      const second = String(Math.floor(Math.random() * 60)).padStart(2, '0');
      
      return {
        id: `${date}-${index}`,
        ...newsContent,
        date: date,
        createdAt: `${date}T${hour}:${minute}:${second}`
      };
    });
    return acc;
  }, {});
  
  // Debug için kontrol logları
  console.log('Today:', formatDate(getCurrentDate()));
  console.log('Available dates in mockNewsData:', Object.keys(mockNewsData).sort());
  console.log('Sample news for latest date:', mockNewsData[dates[dates.length - 1]][0]);
  
  export default mockNewsData;