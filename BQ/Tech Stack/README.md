Moyu:
===

**React** 是一个前端开发库，用来构建网页应用的界面。它的最大特点是把界面拆成很多 组件（Components），就像搭积木一样，把这些小模块组合起来形成一个完整页面。

**Redux** 是一个 状态管理工具(State management tool)，最常搭配 React 使用。它解决的问题是：当应用变得复杂时，页面上不同组件之间要共享和更新数据会很混乱，Redux 就像一个“中央数据仓库”，让所有组件都能从同一个地方拿数据、更新数据。

在我的项目里的作用：
Integrated personalized recommendation results into the user portal using React and Redux to efficiently render over a million item listings, enhancing the overall user experience.

**two-tower model:**

Faiss 当作向量检索引擎来用。

中文
双塔召回模型主要是把用户和物品都映射到同一个向量空间里，然后通过相似度检索来快速筛选候选物品。这样既能保证在上百万物品中实时响应，又能捕捉用户潜在兴趣，为后续精排模型提供候选集。

英文
The two-tower retrieval model maps users and items into the same embedding space and uses similarity search to quickly retrieve candidate items. It enables real-time recommendations at scale while capturing user intent, providing strong candidates for downstream ranking models.

**PostgreSQL:**

PostgreSQL 就是用来存储和更新用户-商品 features、embedding 的数据库，保证数据一致性和高效查询。

**Locust & Kubernetes:**
Locust 是压测工具，帮你模拟用户并发；Kubernetes 是容器管理平台，帮你部署和调度服务。你结合两者，发现并修复了推荐系统的性能问题。

Locust is a load-testing tool that simulates concurrent users, while Kubernetes is a container orchestration platform that manages service deployment and scheduling. By combining both, I was able to identify and fix performance issues in the recommendation system.

**gRPC:**

在你的实习里，gRPC 是各个推荐服务之间交流的“高速通道”，你利用它的 trace 功能定位了性能瓶颈，并据此优化了系统。

During your internship, gRPC served as the "high-speed channel" for communication between recommendation services. You used its trace function to locate performance bottlenecks and optimized the system accordingly.

LightSpeed:
===

**Angular & NgRx:**

Angular：负责搭建和优化前端界面与交互。
NgRx：负责管理应用数据状态，保证界面更新和数据一致性.

In my internship, I used **Angular** to rebuild the tool’s interface, making it easier to use and more responsive. I also used **NgRx** to keep form data consistent across different parts of the app, which helped prevent errors and made updates smoother.

