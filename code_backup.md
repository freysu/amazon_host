## 把Host按域名排序
// host原始数据
const data = ``;

// 将原始数据拆分为行
const lines = data.split('\n');

// 提取域名部分并进行排序
const sortedLines = [...lines]; // 创建原始数据的副本，以免修改原始数据
sortedLines.sort((a, b) => {
  const domainA = (a.match(/(\S+)\s+(\S+)/) || [])[2] || '';
  const domainB = (b.match(/(\S+)\s+(\S+)/) || [])[2] || '';
  return domainA.localeCompare(domainB, undefined, { sensitivity: 'base' });
});

// 输出排序后的结果
console.log(sortedLines.join('\n'));