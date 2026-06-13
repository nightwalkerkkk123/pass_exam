# Effective Java 期末复习资料（完整版）

> 本资料基于《Effective Java》第2~8章PPT内容整理，涵盖 **46条核心条款**，适用于期末复习。

---

## 目录

| 章节 | 条款 | 核心主题 |
|------|------|----------|
| **第2章** | 条款1~7 | 创建和销毁对象 |
| **第3章** | 条款10~14 | 对于所有对象都通用的方法 |
| **第4章** | 条款15~25 | 类和接口 |
| **第5章** | 条款26~33 | 泛型 |
| **第6章** | 条款34~39 | 枚举和注解 |
| **第7章** | 条款42~47 | Lambda和Stream |
| **第8章** | 条款49~55 | 方法 |

---

## 条款速查表

| 条款 | 标题 | 核心要点 |
|------|------|----------|
| 1 | 用静态工厂方法代替构造器 | 有名称、可缓存、可返回子类型、灵活 |
| 2 | 多个构造器参数时用Builder | 重叠构造器 vs JavaBeans vs Builder模式 |
| 3 | 用枚举强化Singleton | 单元素枚举是最佳单例实现方式 |
| 4 | 私有构造器强化不可实例化 | 工具类使用私有构造器 |
| 5 | 优先考虑依赖注入 | 通过构造器传入资源，提升灵活性 |
| 6 | 避免创建不必要的对象 | 重用不可变对象、避免自动装箱 |
| 7 | 消除过期的对象引用 | 手动清空引用防止内存泄漏 |
| 10 | 覆盖equals遵守通用约定 | 五大性质：自反、对称、传递、一致、非空 |
| 11 | 覆盖equals时覆盖hashCode | result = 31*result + c |
| 12 | 始终覆盖toString | 返回简洁、信息丰富、易读的字符串 |
| 13 | 谨慎覆盖clone | 拷贝构造器/拷贝工厂优于clone() |
| 14 | 考虑实现Comparable | compareTo约定、比较器构造方法 |
| 15 | 最小化可访问性 | private > package-private > protected > public |
| 16 | 公有类使用访问方法 | 不要暴露公有可变域 |
| 17 | 最小化可变性 | 不可变类：线程安全、可自由共享 |
| 18 | 复合优先于继承 | 包装类模式避免封装性被破坏 |
| 20 | 接口优于抽象类 | 骨架实现结合两者优点 |
| 21 | 为后代设计接口 | 谨慎设计，缺省方法有风险 |
| 22 | 接口只用于定义类型 | 不用作常量导出 |
| 23 | 类层次优于标签类 | 消除switch，用多态替代 |
| 24 | 优先考虑静态成员类 | 非静态成员类有额外开销 |
| 25 | 限制单个顶级类 | 一个源文件只放一个顶级类 |
| 26 | 不要使用原始类型 | 使用泛型保障类型安全 |
| 27 | 消除非受检警告 | @SuppressWarnings在最小范围使用 |
| 28 | 列表优先于数组 | 数组协变 vs 泛型不可变 |
| 29 | 优先考虑泛型 | 将类泛型化的两种方法 |
| 30 | 优先考虑泛型方法 | 泛型单例工厂、递归类型限制 |
| 31 | 利用有限制的通配符 | PECS：Producer-Extends, Consumer-Super |
| 33 | 类型安全的异构容器 | 键参数化而非容器参数化 |
| 34 | 用enum代替int常量 | 枚举是完整类，类型安全 |
| 35 | 用实例域代替序数 | 不要用ordinal() |
| 36 | 用EnumSet代替位域 | EnumSet内部位向量实现 |
| 37 | 用EnumMap代替序数索引 | 嵌套EnumMap处理二维关系 |
| 38 | 接口模拟可伸缩枚举 | 枚举不可继承，但可实现接口 |
| 39 | 注解优先于命名模式 | 标记注解、元注解、可重复注解 |
| 42 | Lambda优先于匿名类 | 函数接口、类型推导 |
| 43 | 方法引用优先于Lambda | 五种方法引用形式 |
| 44 | 优先使用标准函数接口 | UnaryOperator, Predicate, Function等 |
| 45 | 谨慎使用Stream | 适用场景vs不适用场景 |
| 46 | Stream中无副作用的函数 | 纯函数、Collector |
| 47 | 返回Collection而非Stream | Collection提供更大灵活性 |
| 49 | 检查参数的有效性 | 公有方法检查参数、非公有用断言 |
| 50 | 必要时进行保护性拷贝 | 防止TOCTOU攻击 |
| 51 | 谨慎设计方法签名 | 参数<=4个、用接口、用枚举替代boolean |
| 52 | 明智地使用重载 | 重载静态选择vs覆盖动态选择 |
| 53 | 明智地使用可变参数 | 至少一个参数的正确做法 |
| 54 | 返回零长度数组而非null | 空集合、空数组 |
| 55 | 明智地返回Optional | Optional.of/empty/ofNullable |

---

## 第2章：创建和销毁对象

> **复习要点**：本章围绕对象的创建与销毁，介绍了5个创建对象的条款和2个避免对象滥用的条款，是全书最实用的章节之一。

---

### 条款1：用静态工厂方法代替构造器（Consider static factory methods instead of constructors）

#### 传统构造器方式

```java
public class ClassA {
    public ClassA() {
    }
}
ClassA a = new ClassA();
```

#### 静态工厂方法示例

```java
public static Boolean valueOf(boolean b) {
    return b ? Boolean.TRUE : Boolean.FALSE;
}
```

---

#### 优点1：静态工厂方法有名称

构造器的名称固定为类名，无法表达创建对象的意图；静态工厂方法可以通过名称清晰描述功能。

```java
// 构造器：难以判断返回的是否为素数
public BigInteger(int, int, Random); // 可能返回素数

// 静态工厂方法：名称更加清楚
public static BigInteger BigInteger.probablePrime();
```

> **复习提示**：名称可以传达语义，提高代码可读性。

---

#### 优点2：不必每次调用时都创建新对象

适用于**不可变类（immutable class）**，可以预先创建好实例或缓存实例，反复返回。

```java
// 每次都返回Boolean.TRUE或Boolean.FALSE，不创建新对象
public static Boolean valueOf(boolean b) {
    return b ? Boolean.TRUE : Boolean.FALSE;
}
```

> **复习提示**：类似**享元模式（Flyweight Pattern）**，常用于包装类的`valueOf()`方法。

---

#### 优点3：可返回原返回类型的任何子类型的对象

- 可以返回返回类型的**子类型对象**
- 适用于**基于接口的框架（interface-based frameworks）**
- 可以在不公开具体实现类的情况下返回对象

---

#### 优点4：返回对象的类可根据参数值变化

调用者无需关心返回的是哪个具体子类。

- **`EnumSet`**：根据枚举元素数量决定返回**`RegularEnumSet`**或**`JumboEnumSet`**
  - 元素个数 <= 64 时返回 `RegularEnumSet`（用单个 `long` 存储）
  - 元素个数 > 64 时返回 `JumboEnumSet`（用 `long[]` 存储）

```java
EnumSet.allOf(...);
EnumSet.of(...);
```

---

#### 优点5：在写包含静态工厂方法的类时，返回对象的类可以不存在

- 适用于**Service Provider框架（服务提供者框架）**
- 实现了服务提供者框架的三个核心组件：**服务接口**、**提供者注册API**、**服务访问API**

---

#### Service Provider框架代码示例

```java
// 服务接口
public interface Service {
    // Service-specific methods go here
}

// 提供者接口
public interface Provider {
    Service newService();
}

// 服务管理类（不可实例化）
public class Services {
    private Services() { }  // Prevents instantiation (Item 4)
    
    private static final Map<String, Provider> providers =
        new ConcurrentHashMap<String, Provider>();
    public static final String DEFAULT_PROVIDER_NAME = "<def>";
    
    // 注册默认提供者
    public static void registerDefaultProvider(Provider p) {
        registerProvider(DEFAULT_PROVIDER_NAME, p);
    }
    
    // 注册命名提供者
    public static void registerProvider(String name, Provider p) {
        providers.put(name, p);
    }
    
    // 获取默认服务实例（服务访问API）
    public static Service newInstance() {
        return newInstance(DEFAULT_PROVIDER_NAME);
    }
    
    // 获取指定名称的服务实例
    public static Service newInstance(String name) {
        Provider p = providers.get(name);
        if (p == null)
            throw new IllegalArgumentException(
                "No provider registered with name: " + name);
        return p.newService();
    }
}
```

> **复习提示**：JDBC就是典型的Service Provider框架，`Connection`是服务接口，`DriverManager.registerDriver()`是提供者注册API，`DriverManager.getConnection()`是服务访问API。

---

#### 缺点

| 缺点 | 说明 |
|------|------|
| **不能被子类化** | 类如果不含公有或受保护的构造器，不能被子类化（但这也可能促使程序员多用组合而非继承） |
| **难以辨别** | 程序员难以发现静态工厂方法的存在（构造器在API文档中更醒目） |

---

#### 静态工厂方法的惯用名称

| 名称 | 说明 | 示例 |
|------|------|------|
| **`from`** | 类型转换 | `Date d = Date.from(instant);` |
| **`of`** | 聚合多个参数 | `Set<Rank> faceCards = EnumSet.of(JACK, QUEEN, KING);` |
| **`valueOf`** | 与`from`/`of`类似，常作类型转换 | `BigInteger.valueOf(Integer.MAX_VALUE);` |
| **`instance` / `getInstance`** | 返回实例（可能为新实例或缓存实例） | `StackWalker luke = StackWalker.getInstance(options);` |
| **`create` / `newInstance`** | 每次返回新实例 | `Object newArray = Array.newInstance(classObject, arrayLen);` |
| **`getType`** | 工厂方法在别的类中 | `FileStore fs = Files.getFileStore(path);` |
| **`newType`** | 工厂方法在别的类中，每次返回新实例 | `BufferedReader br = Files.newBufferedReader(path);` |
| **`type`** | `getType`和`newType`的简洁替代 | `List<Complaint> litany = Collections.list(legacyLitany);` |

---

### 条款2：遇到多个构造器参数时考虑使用构建器（Consider a builder when faced with many constructor parameters）

#### 问题背景

静态工厂和构造器有一个局限性：**不能对大量可选参数进行很好的扩展**。

例如：食品的营养标签，有多个必需参数和可选参数。

```java
public class NutritionFacts {
    private final int servingSize;   // (mL) required - 每份含量
    private final int servings;      // (per container) required - 每容器份数
    private final int calories;      // optional - 卡路里
    private final int fat;           // (g) optional - 脂肪
    private final int sodium;        // (mg) optional - 钠
    private final int carbohydrate;  // (g) optional - 碳水化合物
}
```

---

#### 方案一：重叠构造器模式（Telescoping Constructor）

提供多个构造器，参数从少到多逐步叠加。

```java
public NutritionFacts(int servingSize, int servings) { ... }
public NutritionFacts(int servingSize, int servings, int calories) { ... }
public NutritionFacts(int servingSize, int servings, int calories, int fat) { ... }
// ... 更多构造器
```

**缺点**：
- 参数过多时，**较难编写**
- 使用时**容易出错**（需要传递大量参数，容易混淆参数顺序）
- 代码难以阅读和维护

---

#### 方案二：JavaBeans模式

先调用无参构造器，然后通过setter方法设置属性。

```java
public class NutritionFacts {
    private int servingSize = -1;
    private int servings = -1;
    private int calories = 0;
    // Setters...
}

// 使用方式
NutritionFacts cocaCola = new NutritionFacts();
cocaCola.setServingSize(240);
cocaCola.setServings(8);
cocaCola.setCalories(100);
```

**缺点**：
1. **不能构造不可变类**（需要setter方法，属性不能设为final）
2. **构造被分成了多次调用**，对象处于不一致状态
3. **实例在使用时可能不一致**（某些必要参数尚未设置）
4. 类无法通过检查构造参数的有效性来保证一致性

---

#### 方案三：Builder模式（推荐）

结合了重叠构造器的安全性和JavaBeans模式的易读性。

```java
public class NutritionFacts {
    private final int servingSize;
    private final int servings;
    private final int calories;
    private final int fat;
    private final int sodium;
    private final int carbohydrate;
    
    public static class Builder {
        // 必需参数
        private final int servingSize;
        private final int servings;
        
        // 可选参数（带有默认值）
        private int calories = 0;
        private int fat = 0;
        private int sodium = 0;
        private int carbohydrate = 0;
        
        public Builder(int servingSize, int servings) {
            this.servingSize = servingSize;
            this.servings = servings;
        }
        
        public Builder calories(int val) { 
            calories = val; 
            return this; 
        }
        public Builder fat(int val) { 
            fat = val; 
            return this; 
        }
        public Builder sodium(int val) { 
            sodium = val; 
            return this; 
        }
        public Builder carbohydrate(int val) { 
            carbohydrate = val; 
            return this; 
        }
        
        public NutritionFacts build() { 
            return new NutritionFacts(this); 
        }
    }
    
    private NutritionFacts(Builder builder) {
        servingSize = builder.servingSize;
        servings = builder.servings;
        calories = builder.calories;
        fat = builder.fat;
        sodium = builder.sodium;
        carbohydrate = builder.carbohydrate;
    }
}
```

**使用方式**（流式API / Fluent API）：

```java
NutritionFacts cocaCola = new NutritionFacts.Builder(240, 8)
    .calories(100)
    .sodium(35)
    .carbohydrate(27)
    .build();
```

> **复习提示**：Builder模式的关键在于**内部类Builder的每个setter方法都返回this**，从而实现方法链式调用。build()方法最后调用私有构造器完成对象创建。

---

#### Builder模式适用于类层次结构

Builder模式可以用**平行层次结构**的方式适用于类层次结构（abstract class有abstract builder，concrete class有concrete builder）。

**Pizza层次结构示例**：

```java
// 抽象Pizza类
public abstract class Pizza {
    public enum Topping { HAM, MUSHROOM, ONION, PEPPER, SAUSAGE }
    final Set<Topping> toppings;
    
    // 带有递归类型参数的Builder
    abstract static class Builder<T extends Builder<T>> {
        EnumSet<Topping> toppings = EnumSet.noneOf(Topping.class);
        
        public T addTopping(Topping topping) {
            toppings.add(Objects.requireNonNull(topping));
            return self();
        }
        
        abstract Pizza build();
        
        // 子类必须重写这个方法返回"this"
        protected abstract T self();
    }
    
    Pizza(Builder<?> builder) {
        toppings = builder.toppings.clone();
    }
}

// 具体Pizza类 - 纽约风味
public class NyPizza extends Pizza {
    public enum Size { SMALL, MEDIUM, LARGE }
    private final Size size;
    
    public static class Builder extends Pizza.Builder<Builder> {
        private final Size size;
        
        public Builder(Size size) {
            this.size = Objects.requireNonNull(size);
        }
        
        @Override public NyPizza build() {
            return new NyPizza(this);
        }
        
        @Override protected Builder self() { return this; }
    }
    
    private NyPizza(Builder builder) {
        super(builder);
        size = builder.size;
    }
}

// 具体Pizza类 - 意大利风味
public class Calzone extends Pizza {
    private final boolean sauceInside;
    
    public static class Builder extends Pizza.Builder<Builder> {
        private boolean sauceInside = false;
        
        public Builder sauceInside() {
            sauceInside = true;
            return this;
        }
        
        @Override public Calzone build() {
            return new Calzone(this);
        }
        
        @Override protected Builder self() { return this; }
    }
    
    private Calzone(Builder builder) {
        super(builder);
        sauceInside = builder.sauceInside;
    }
}

// 使用方式
NyPizza pizza = new NyPizza.Builder(SMALL)
    .addTopping(SAUSAGE)
    .addTopping(ONION)
    .build();

Calzone calzone = new Calzone.Builder()
    .addTopping(HAM)
    .sauceInside()
    .build();
```

> **复习提示**：类层次结构中Builder模式的核心技巧是**带有递归类型参数的Builder**（`Builder<T extends Builder<T>>`）和 **`self()`方法**，这样子类builder可以链式调用父类的setter方法。

---

#### Builder模式的缺点

- 为了创建对象，必须**先创建Builder对象**，引入了额外的开销
- 如果参数很少（如4个或更少），Builder模式可能不如重叠构造器或静态工厂方法简洁
- 适用于**参数较多（通常 >= 4个）**的情况

> **复习要点总结**：
> - 参数少（<= 3个）：用重叠构造器或静态工厂
> - 参数多（>= 4个）：优先用Builder模式
> - 需要不可变类：不能用JavaBeans模式，考虑Builder模式

---

### 条款3：用私有构造器或枚举类型强化Singleton属性（Enforce the singleton property with a private constructor or an enum type）

**Singleton（单例）**：只实例化一次的类。

适用场景：无状态的对象（如函数）、系统组件。

---

#### 方法一：公有静态成员是final域

```java
public class Elvis {
    public static final Elvis INSTANCE = new Elvis();
    
    private Elvis() { }
    
    public void leaveTheBuilding() { ... }
}
```

**优点**：
- 易于识别（`INSTANCE`字段明确表示这是一个单例）
- 实现简单

**注意**：私有构造器可以被反射攻击调用（ AccessibleObject.setAccessible），如果要防御，可以在构造器中抛出异常。

---

#### 方法二：公有成员是静态工厂方法

```java
public class Elvis {
    private static final Elvis INSTANCE = new Elvis();
    
    private Elvis() { }
    
    public static Elvis getInstance() { 
        return INSTANCE; 
    }
    
    public void leaveTheBuilding() { ... }
}
```

**优点**：
- **灵活性**：可以更改实现（如改为每个线程一个实例）而不影响API
- 可以编写**泛型单例工厂（generic singleton factory）**
- 可以通过**方法引用（method reference）**作为提供者，如 `Elvis::getInstance` 可作为 `Supplier<Elvis>`

---

#### 方法三：包含单个元素的枚举类型（最佳方法）

```java
public enum Elvis {
    INSTANCE;
    
    public void leaveTheBuilding() { ... }
}
```

**优点**：
- 更简洁
- **默认提供了序列化机制**
- 绝对防止多次实例化（即使面对反射攻击和序列化）
- **是实现单例的最佳方法**

**局限**：如果单例类必须继承某个超类，则不能使用枚举方法（Java枚举类型不能继承其他类，只能实现接口）。

> **复习提示**：在大多数情况下，**单元素枚举类型是实现Singleton的最佳方式**。只有当类必须继承某个超类时，才考虑使用final域或静态工厂方法。

---

### 条款4：通过私有构造器强化不可实例化的能力（Enforce noninstantiability with a private constructor）

有些类只包含静态方法和静态字段，是**工具类（utility class）**，无需实例化。

示例：`java.lang.Math`、`java.util.Arrays`、`java.util.Collections`

---

#### 错误做法：抽象类

将类声明为抽象类并不能阻止实例化（子类可以实例化），且容易误导用户认为该类是为了继承而设计的。

---

#### 正确做法：私有构造器

```java
public class UtilityClass {
    // 私有构造器，阻止实例化
    private UtilityClass() {
        throw new AssertionError(); // 防止在类内部意外调用
    }
    
    // 静态方法和字段...
}
```

**要点**：
- 显式私有构造器阻止类被外部实例化
- 在构造器中抛出 `AssertionError`，防止类内部意外调用
- 注释说明构造器的用途

---

### 条款5：优先考虑依赖注入来引用资源（Prefer dependency injection to hardwire resources）

#### 问题

**静态工具类**和**单例实现**都**只可支持单一资源**，行为被硬编码，缺乏灵活性。

#### 解决方案：依赖注入（Dependency Injection）

创建新实例时，将所依赖的**资源（resource）**传入构造器。

```java
public class SpellChecker {
    private final Lexicon dictionary;
    
    // 依赖注入：通过构造器传入资源
    public SpellChecker(Lexicon dictionary) {
        this.dictionary = Objects.requireNonNull(dictionary);
    }
    
    public boolean isValid(String word) { ... }
    public List<String> suggestions(String typo) { ... }
}
```

**优点**：
- 类可**多次实例化**，支持**多资源**
- 极大地提升了类的**灵活性**、**可重用性**和**可测试性**
- 可以使用**mock资源**进行单元测试
- 依赖注入框架（Spring, Guice, Dagger）可以简化大型项目的依赖管理

> **复习提示**：简单地说，当类依赖某个底层资源时，**不要把资源的创建直接写在类里面**（静态工具类/单例），而应该**通过构造器（或setter/接口）将资源传入**。这就是依赖注入的核心思想。

---

### 条款6：避免创建不必要的对象（Avoid creating unnecessary objects）

#### 1. 重用不可变的对象

**字符串字面常量**：
```java
// 正确：使用字符串字面常量（JVM会自动池化）
String s = "bikini";

// 错误：每次调用都创建新实例
String s = new String("bikini"); // DON'T DO THIS!
```

**优先使用静态工厂方法**：
```java
// 正确：使用valueOf，可能返回缓存实例
Boolean.valueOf(String);

// 错误：每次创建新对象（Java 9中已废弃）
new Boolean(String);  // DEPRECATED
```

---

#### 2. 重用已知不会被修改的可变对象

**示例1：罗马数字判定** — 预编译Pattern vs 每次调用matches()

```java
// 错误做法：每次调用都创建Pattern实例
static boolean isRomanNumeral(String s) {
    return s.matches("^(?=.)M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$");
}

// 正确做法：预编译Pattern，只创建一次
public class RomanNumerals {
    private static final Pattern ROMAN = Pattern.compile(
        "^(?=.)M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$");
    
    static boolean isRomanNumeral(String s) {
        return ROMAN.matcher(s).matches();
    }
}
```

> **复习提示**：`String.matches()`方法内部会创建`Pattern`实例，且只使用一次就丢弃，如果在循环中调用会产生大量不必要的对象。

---

**示例2：`isBabyBoomer`** — 使用`static`初始化块预计算日期

```java
public class Person {
    private final Date birthDate;
    
    // 这些Date对象只需创建一次
    private static final Date BOOM_START;
    private static final Date BOOM_END;
    
    // 静态初始化块
    static {
        Calendar gmtCal = Calendar.getInstance(TimeZone.getTimeZone("GMT"));
        gmtCal.set(1946, Calendar.JANUARY, 1, 0, 0, 0);
        BOOM_START = gmtCal.getTime();
        gmtCal.set(1965, Calendar.JANUARY, 1, 0, 0, 0);
        BOOM_END = gmtCal.getTime();
    }
    
    public boolean isBabyBoomer() {
        return birthDate.compareTo(BOOM_START) >= 0
            && birthDate.compareTo(BOOM_END) < 0;
    }
}
```

> **复习要点**：如果对象创建成本高，且已知不会被修改，应在**静态初始化块**中创建并缓存，避免重复创建。

---

#### 3. 避免无意识的自动装箱（Autoboxing）

**自动装箱（autoboxing）**允许基本类型和包装类型混用，但会隐含地创建对象。

```java
// 极其缓慢！每次sum += i都会导致Long的自动装箱拆箱
private static long sum() {
    Long sum = 0L;  // 包装类型
    for (long i = 0; i <= Integer.MAX_VALUE; i++)
        sum += i;   // 每次循环都创建新的Long对象！
    return sum;
}
```

**修正**：使用基本类型声明变量：
```java
private static long sum() {
    long sum = 0L;  // 基本类型
    for (long i = 0; i <= Integer.MAX_VALUE; i++)
        sum += i;   // 无自动装箱
    return sum;
}
```

> **复习提示**：**优先使用基本类型而非包装类型**，注意无意识的自动装箱。这条规则适用于反复执行的循环等性能敏感场景。

---

### 条款7：消除过期的对象引用（Eliminate obsolete object references）

#### Java垃圾回收 vs C++手工管理

- Java有**垃圾回收（GC）**功能，但**并不意味着不会内存泄漏**
- 只要对象引用仍然存在，GC就不会回收该对象

---

#### 示例：Stack的pop()方法

```java
public Object pop() {
    if (size == 0)
        throw new EmptyStackException();
    Object result = elements[--size];
    elements[size] = null; // 消除过期引用
    return result;
}
```

**问题**：如果不将`elements[size]`设为`null`，从栈中弹出的对象将不会被GC回收，因为栈内部仍然持有这些对象的引用。这会导致**内存泄漏**。

**修正**：在弹出元素后，**清空引用** `elements[size] = null`。

> **复习提示**：当元素被"主动弹出"时，数组槽中的引用变成了**过期引用（obsolete reference）**——永远不会再被解除引用，但GC不知道这一点。

---

#### 清空对象引用不是规范行为

- **清空对象引用应该是例外，而不是规范**
- 过度使用会使代码冗长、降低可读性

**更好的做法**：在**紧凑的使用作用域范围内定义变量**，让它们自然超出作用域。

```java
// 使用局部作用域
{
    Object a = new Object();
    // do something
} // a在这里超出作用域，引用自然消除
```

#### 何时应该手动清空引用？

| 场景 | 说明 |
|------|------|
| **类自己管理内存** | 如Stack、数组实现的容器类 |
| **缓存** | 对象放入缓存后容易被遗忘，可使用`WeakHashMap` |
| **监听器和回调** | 注册后忘记取消注册，可使用弱引用 |

> **复习要点**：内存泄漏常见来源：
> 1. 自己管理内存的类（如Stack）中的过期引用
> 2. 缓存（对象放入缓存后再也不会被读取）
> 3. 监听器和其他回调（注册后没有显式取消）

---

## 第3章：对于所有对象都通用的方法

> **复习要点**：本章围绕Object类的通用方法（equals, hashCode, toString, clone）和Comparable接口（compareTo），讲解如何正确覆盖这些方法。这是面试和考试的高频考点。

---

### 通用方法概览

| 来源 | 方法 | 用途 |
|------|------|------|
| `Object`类 | `equals` | 判断两个实例是否逻辑相等 |
| `Object`类 | `hashCode` | 返回对象的哈希码 |
| `Object`类 | `toString` | 返回对象的字符串表示 |
| `Object`类 | `clone` | 创建并返回对象的副本 |
| `Comparable<T>`接口 | `compareTo` | 比较对象的大小关系 |

---

### 条款10：覆盖equals时遵守通用约定（Obey the general contract when overriding equals）

#### 什么时候无需覆盖equals？

| 情况 | 示例 | 说明 |
|------|------|------|
| 每个实例确实是唯一的 | `Thread` | 代表活动实体而非值 |
| 不关心逻辑相等 | `Random`、`Pattern` | 无需比较 |
| 超类已覆盖且适用子类 | `Set`、`List` | 继承父类行为即可 |
| 类或包是私有的 | 内部工具类 | 不会被子类化或外部使用 |

---

#### 什么时候需要覆盖equals？

当类具有**"逻辑相等（logical equality）"**的概念，且父类没有正确覆盖equals时。

- **值类（value classes）**：`Integer`、`String`、`Date`
- 程序员需要比较两个实例在逻辑上是否相等

---

#### equals方法的通用约定

覆盖equals方法时，必须遵守以下**五大性质**：

| 性质 | 数学术语 | 定义 |
|------|----------|------|
| **自反性** | Reflexive | `x.equals(x)` 必须返回 `true` |
| **对称性** | Symmetric | `x.equals(y)` 与 `y.equals(x)` 返回值必须相同 |
| **传递性** | Transitive | `x.equals(y)` 且 `y.equals(z)`，则 `x.equals(z)` |
| **一致性** | Consistent | 信息未变时，多次调用返回值一致 |
| **非空性** | Non-nullity | `x.equals(null)` 必须返回 `false` |

> **考试重点**：违反任何一条都会导致严重问题！尤其是**对称性**和**传递性**在继承场景中容易违反。

---

#### 对称性示例：CaseInsensitiveString

**违反对称性的实现**：

```java
// 错误实现！违反了对称性
public final class CaseInsensitiveString {
    private final String s;
    
    public CaseInsensitiveString(String s) {
        this.s = Objects.requireNonNull(s);
    }
    
    @Override
    public boolean equals(Object o) {
        if (o instanceof CaseInsensitiveString)
            return s.equalsIgnoreCase(((CaseInsensitiveString) o).s);
        // 这一行破坏了对称性！
        if (o instanceof String)
            return s.equalsIgnoreCase((String) o);
        return false;
    }
}
```

**问题**：
```java
CaseInsensitiveString cis = new CaseInsensitiveString("Polish");
String s = "polish";

cis.equals(s); // true
s.equals(cis); // false（String.equals不认识CaseInsensitiveString）
// 违反对称性！
```

**修正**：不要尝试与不同类混用比较。

```java
@Override
public boolean equals(Object o) {
    // 只与同类型比较
    return o instanceof CaseInsensitiveString &&
        ((CaseInsensitiveString) o).s.equalsIgnoreCase(s);
}
```

---

#### 传递性示例：Point与ColorPoint

**问题**：使用继承添加颜色属性时，equals无法满足传递性。

```java
public class Point {
    private final int x;
    private final int y;
    
    @Override public boolean equals(Object o) {
        if (!(o instanceof Point)) return false;
        Point p = (Point) o;
        return p.x == x && p.y == y;
    }
}

// 继承Point并添加颜色
public class ColorPoint extends Point {
    private final Color color;
    
    // 错误做法1：忽略颜色 - 违反自反性/对称性
    // 错误做法2：混合比较 - 违反传递性！
    @Override public boolean equals(Object o) {
        if (!(o instanceof Point)) return false;
        // 如果o是普通Point，只比较坐标（忽略颜色）
        if (!(o instanceof ColorPoint))
            return o.equals(this); // 调用Point.equals
        // 如果o是ColorPoint，比较坐标和颜色
        return super.equals(o) && ((ColorPoint) o).color == color;
    }
}
```

**传递性被破坏**：
```java
ColorPoint p1 = new ColorPoint(1, 2, Color.RED);
Point p2 = new Point(1, 2);
ColorPoint p3 = new ColorPoint(1, 2, Color.BLUE);

p1.equals(p2); // true（ColorPoint忽略颜色与Point比较）
p2.equals(p3); // true（Point.equals只比较坐标）
p1.equals(p3); // false（颜色不同）→ 违反传递性！
```

---

#### 解决方案：利用复合而不是继承（Favor composition over inheritance）

```java
// 不使用继承，而是将Point作为ColorPoint的组件
public class ColorPoint {
    private final Point point;  // 复合
    private final Color color;
    
    public ColorPoint(int x, int y, Color color) {
        point = new Point(x, y);
        this.color = Objects.requireNonNull(color);
    }
    
    // 返回底层的Point视图
    public Point asPoint() {
        return point;
    }
    
    @Override public boolean equals(Object o) {
        if (!(o instanceof ColorPoint)) return false;
        ColorPoint cp = (ColorPoint) o;
        return cp.point.equals(point) && cp.color.equals(color);
    }
    
    @Override public int hashCode() {
        return 31 * point.hashCode() + color.hashCode();
    }
}
```

> **复习要点**：在equals方法中使用`getClass()`进行判断虽然可以满足所有约定，但违反了**里氏替换原则（Liskov Substitution Principle）**。最佳实践是**不要继承值类**，改用**复合（composition）**。

---

#### 高质量equals方法的编写步骤

```java
@Override
public boolean equals(Object o) {
    // Step 1: 使用 == 检查是否引用同一对象
    if (o == this) return true;
    
    // Step 2: 使用 instanceof 检查类型
    if (!(o instanceof PhoneNumber)) return false;
    
    // Step 3: 强制类型转换
    PhoneNumber pn = (PhoneNumber) o;
    
    // Step 4: 比较所有关键域
    return pn.lineNum == lineNum && pn.prefix == prefix && pn.areaCode == areaCode;
}
```

**完整示例：PhoneNumber的equals实现**

```java
public final class PhoneNumber {
    private final short areaCode, prefix, lineNum;
    
    public PhoneNumber(int areaCode, int prefix, int lineNum) {
        this.areaCode = rangeCheck(areaCode, 999, "area code");
        this.prefix = rangeCheck(prefix, 999, "prefix");
        this.lineNum = rangeCheck(lineNum, 9999, "line num");
    }
    
    private static short rangeCheck(int val, int max, String arg) {
        if (val < 0 || val > max)
            throw new IllegalArgumentException(arg + ": " + val);
        return (short) val;
    }
    
    @Override 
    public boolean equals(Object o) {
        if (o == this) return true;
        if (!(o instanceof PhoneNumber)) return false;
        PhoneNumber pn = (PhoneNumber) o;
        return pn.lineNum == lineNum && pn.prefix == prefix && pn.areaCode == areaCode;
    }
    
    @Override public int hashCode() { ... }  // 见条款11
    @Override public String toString() { ... } // 见条款12
}
```

---

#### 覆盖equals的注意事项

1. **覆盖equals时总要覆盖hashCode**（条款11）
2. **不要将equals声明中的Object替换为其他类型** — 这是重载（overload）而非覆盖（override），会导致隐蔽的bug
   ```java
   // 错误！这是重载，不是覆盖
   public boolean equals(MyClass o) { ... }
   
   // 正确！这才是覆盖
   @Override
   public boolean equals(Object o) { ... }
   ```
3. 使用`@Override`注解可以避免此类错误

---

### 条款11：覆盖equals时要覆盖hashCode（Always override hashCode when you override equals）

#### hashCode通用约定

| 约定 | 说明 |
|------|------|
| **一致性** | 同一对象多次调用`hashCode()`，返回值必须一致（前提：equals比较所用信息未修改） |
| **equals相等则hashCode相等** | 两个对象通过`equals`比较相等，则它们的`hashCode`返回值必须相同 |
| **equals不等hashCode可以相等** | 两个对象通过`equals`比较不等，它们的`hashCode`返回值可以相同（但最好不同，以提高哈希表性能） |

> **核心原则**：**equals相等 → hashCode必须相等**。违反这条会导致基于哈希的集合（`HashMap`、`HashSet`、`HashTable`）无法正常工作。

---

#### hashCode实现方法

**通用公式**：
```java
// 1. 初始化result为非零常数（通常是17或1）
int result = Integer.hashCode(areaCode);

// 2. 对每一个关键域f，计算其哈希码c
// 3. 合并：result = 31 * result + c
result = 31 * result + Integer.hashCode(prefix);
result = 31 * result + Integer.hashCode(lineNum);

return result;
```

**选择31的原因**：
- 31是**奇素数**
- `31 * i == (i << 5) - i`，JVM可以优化为位移运算
- 有助于产生较少的哈希冲突

---

#### 各类型域的哈希码计算

| 域类型 | 哈希码计算方式 |
|--------|---------------|
| `boolean` | `f ? 1 : 0` |
| `byte`, `short`, `char`, `int` | `(int) f` |
| `long` | `(int)(f ^ (f >>> 32))` |
| `float` | `Float.hashCode(f)` |
| `double` | `Double.hashCode(f)` |
| 对象引用 | `f == null ? 0 : f.hashCode()` |
| 数组 | `Arrays.hashCode(array)` |

---

#### PhoneNumber的hashCode实现

```java
// 方法一：标准实现
@Override
public int hashCode() {
    int result = Short.hashCode(areaCode);
    result = 31 * result + Short.hashCode(prefix);
    result = 31 * result + Short.hashCode(lineNum);
    return result;
}

// 方法二：使用Objects.hash()（简洁但性能稍差）
@Override
public int hashCode() {
    return Objects.hash(areaCode, prefix, lineNum);
}
```

---

#### 注意事项

1. **忽略冗余域**：不要包含equals中未使用的域
2. **缓存hashCode**（延迟初始化）：如果类是不可变的且hashCode计算成本高，可以缓存
   ```java
   private int hashCode; // 默认为0
   
   @Override
   public int hashCode() {
       int result = hashCode;
       if (result == 0) { // 延迟初始化
           result = Short.hashCode(areaCode);
           result = 31 * result + Short.hashCode(prefix);
           result = 31 * result + Short.hashCode(lineNum);
           hashCode = result;
       }
       return result;
   }
   ```

---

### 条款12：始终要覆盖toString（Always override toString）

#### Object默认实现

```java
// 默认实现：类名 + @ + 无符号十六进制哈希码
getClass().getName() + "@" + Integer.toHexString(hashCode())
// 例如：PhoneNumber@163b91
```

---

#### 为什么要覆盖toString？

- 默认实现几乎不包含任何有用信息
- `toString()`方法被**隐式调用**于打印语句、调试器、日志记录等场景
- 好的`toString()`可以使类更易于使用、更易于调试

---

#### toString应该返回什么？

- **简洁、信息丰富、易于阅读的字符串**
- 应该返回对象中**值得关注的信息**

```java
@Override
public String toString() {
    return String.format("%03d-%03d-%04d", areaCode, prefix, lineNum);
    // 输出：707-867-5309
}
```

---

#### 是否应指定toString的格式？

| 方案 | 优点 | 缺点 |
|------|------|------|
| **指定格式** | 可用作标准、可持久化 | 一旦指定，终身受限于该格式 |
| **不指定格式** | 灵活性高 | 信息可能不稳定 |

**建议**：无论是否指定格式，都应该在文档中**明确说明意图**。

---

#### 为toString返回值中的信息提供访问途径

如果`toString()`返回了对象的详细信息，应提供相应的getter方法，避免程序员从字符串中解析。

```java
// 不好的做法：让程序员从字符串中解析
String s = phoneNumber.toString();
String areaCode = s.substring(0, 3); // 脆弱！

// 好的做法：提供getter
public int getAreaCode() { return areaCode; }
public int getPrefix() { return prefix; }
public int getLineNum() { return lineNum; }
```

---

### 条款13：谨慎覆盖clone（Override clone judiciously）

#### Cloneable接口的问题

- `Cloneable`接口是Java的一个**设计缺陷** — 它是一个**空接口（marker interface）**，改变了`Object.clone()`的行为
- 实现了`Cloneable`接口的类，`Object.clone()`会返回该对象的逐域拷贝
- 未实现`Cloneable`接口的类调用`clone()`会抛出`CloneNotSupportedException`

---

#### 浅拷贝（Shallow Copy）与深拷贝（Deep Copy）

| 类型 | 说明 | 问题 |
|------|------|------|
| **浅拷贝** | 拷贝对象本身，但引用类型域仍指向原对象中的对象 | 修改拷贝会影响原对象 |
| **深拷贝** | 递归拷贝对象及其所有引用对象 | 实现复杂，可能有循环引用问题 |

---

#### 正确实现clone的方式

```java
@Override
public PhoneNumber clone() {
    try {
        return (PhoneNumber) super.clone();
    } catch (CloneNotSupportedException e) {
        throw new AssertionError(); // 不会发生
    }
}
```

---

#### 处理可变引用类型域

对于包含可变引用类型域的类，需要**递归调用clone()**或手动拷贝。

```java
@Override
public Stack clone() {
    try {
        Stack result = (Stack) super.clone();
        result.elements = elements.clone(); // 深拷贝数组
        return result;
    } catch (CloneNotSupportedException e) {
        throw new AssertionError();
    }
}
```

> **注意**：`elements.clone()`的结果需要强制转换为正确的数组类型，但编译时无法检查。这是Java数组实现的局限。

---

#### 拷贝构造器和拷贝工厂（更好的替代方案）

**不推荐使用clone()**，更好的方式是使用**拷贝构造器（copy constructor）**或**拷贝工厂（copy factory）**。

```java
// 拷贝构造器
public Y(Y y);  

// 拷贝工厂
public static Y newInstance(Y y);
```

**优点**：
- 不依赖于有风险的克隆机制
- 不强制遵循extralinguistic conventions（文档之外的约定）
- 不会与final域产生冲突
- 可以进行类型转换
- 可以接收接口类型参数（更灵活）

```java
// 拷贝工厂接收接口类型参数 — 更灵活
public HashSet(Set<T> s); // 可以接受任何Set实现
```

> **复习要点**：最佳实践是**不要实现Cloneable接口**，使用拷贝构造器或拷贝工厂来替代。对于不可变类，无需拷贝功能。

---

### 条款14：考虑实现Comparable接口（Consider implementing Comparable）

#### compareTo方法的约定

实现了`Comparable<T>`接口的类，可以表明其**实例具有内在的排序关系**。

**compareTo方法的通用约定**：

| 返回值 | 含义 |
|--------|------|
| `< 0`（负数） | `this < o`（当前对象小于参数对象） |
| `== 0`（零） | `this == o`（当前对象等于参数对象） |
| `> 0`（正数） | `this > o`（当前对象大于参数对象） |

**五大性质**（与equals类似）：

| 性质 | 定义 |
|------|------|
| **自反性** | `sgn(x.compareTo(y)) == -sgn(y.compareTo(x))` |
| **传递性** | `x.compareTo(y) > 0` 且 `y.compareTo(z) > 0`，则 `x.compareTo(z) > 0` |
| **一致性** | 信息未变时，多次调用结果一致 |
| **与equals一致**（强烈建议） | `x.compareTo(y) == 0` 则 `x.equals(y)` 应为 `true` |

---

#### BigDecimal：compareTo与equals不一致的陷阱

```java
BigDecimal a = new BigDecimal("1.0");
BigDecimal b = new BigDecimal("1.00");

a.compareTo(b); // 0（相等）
a.equals(b);    // false（不相等，精度不同）
```

这会导致`TreeSet`（使用compareTo）和`HashSet`（使用equals）中的行为不一致。

---

#### 比较器构造方法（Java 8+）

Java 8引入了比较器构造方法，使实现`Comparable`更加简洁。

```java
// 使用comparingInt提取比较键
Comparator<PhoneNumber> byAreaCode = Comparator.comparingInt(pn -> pn.areaCode);

// 多级比较：先比较areaCode，再比较prefix，最后比较lineNum
Comparator<PhoneNumber> comp = Comparator
    .comparingInt((PhoneNumber pn) -> pn.areaCode)
    .thenComparingInt(pn -> pn.prefix)
    .thenComparingInt(pn -> pn.lineNum);
```

---

#### 避免基于差值的Comparator（防止整数溢出）

```java
// 错误！可能导致整数溢出
Comparator<Integer> wrong = (i, j) -> i - j;
// Integer.MIN_VALUE - 1 会导致溢出！

// 正确做法1：使用Integer.compare()
Comparator<Integer> correct = (i, j) -> Integer.compare(i, j);

// 正确做法2：使用Comparator.comparingInt()
Comparator<Integer> correct2 = Comparator.comparingInt(i -> i);

// 正确做法3：使用自然排序
Comparator<Integer> correct3 = Comparator.naturalOrder();
```

> **复习要点**：永远不要使用基于差值的比较器（`i - j`），因为可能导致整数溢出。使用`Integer.compare()`或比较器构造方法。

---

## 第2-3章复习总结

### 第2章核心知识点

| 条款 | 核心内容 |
|------|----------|
| **条款1** | 静态工厂方法的5个优点、2个缺点、8个惯用名称 |
| **条款2** | 重叠构造器 vs JavaBeans vs Builder模式；Builder模式适用于类层次结构 |
| **条款3** | 三种Singleton实现方式；**单元素枚举是最佳方法** |
| **条款4** | 工具类使用**私有构造器**强化不可实例化 |
| **条款5** | **依赖注入**使类支持多资源，提升灵活性和可测试性 |
| **条款6** | 避免不必要对象：重用不可变对象、避免无意识自动装箱 |
| **条款7** | 消除过期引用防止内存泄漏；三种泄漏来源 |

### 第3章核心知识点

| 条款 | 核心内容 |
|------|----------|
| **条款10** | equals的**五大约定**（自反、对称、传递、一致、非空）；复合优于继承 |
| **条款11** | **覆盖equals必须覆盖hashCode**；`result = 31 * result + c` |
| **条款12** | 始终覆盖toString；提供简洁、信息丰富的字符串表示 |
| **条款13** | 谨慎使用clone；优先使用**拷贝构造器/拷贝工厂** |
| **条款14** | Comparable的compareTo约定；**避免基于差值的比较器** |

---

> **最后提示**：第2章是全书最实用的章节，Builder模式、单例、依赖注入都是高频考点和面试重点。第3章的equals和hashCode的约定是Java编程基础中的重中之重，几乎每次考试和面试都会涉及。


---

## 第4章：类和接口

> **复习要点**：本章围绕类的设计与接口使用，涵盖封装、可变性、继承与复合、接口设计等核心主题。重点掌握**最小化可访问性**和**最小化可变性**两大原则。

---

### 条款15：使类和成员的可访问性最小化

#### 信息隐藏与封装

- **信息隐藏（Information Hiding）/ 封装（Encapsulation）**：各模块隐藏其实现细节，通过**API**进行通信
- 好处：
  1. **解除耦合关系** —— 模块之间互不影响
  2. **独立开发、测试、优化** —— 可以并行工作
  3. **提高可重用性** —— 模块可独立复用

> **核心原则**：尽可能使每个类或成员不被外界访问。

#### 顶层类和接口的可访问性

| 修饰符 | 访问范围 | 说明 |
|--------|----------|------|
| 无修饰符（默认） | **包级私有（package-private）** | 只被包内使用 |
| `public` | **公有** | 包导出的API的一部分，后续版本需永久支持 |

> **复习提示**：若一个包级私有顶层类只在另一个类内部用到，应将其改为该类的**私有嵌套类**，进一步降低可访问性。

#### 成员的可访问性

可访问性由小到大排列：

```
私有的（private）→ 包级私有（默认）→ 受保护的（protected）→ 公有的（public）
```

关键规则：
- **尽量减少包级私有和受保护成员**的数量
- **实例域绝不能是公有的**（除非是静态 final 常量）
- 静态 final 常量可以为公有，但**不能为可变对象的引用**

```java
// 错误：公有的可变数组域
public static final Thing[] VALUES = { ... };

// 正确：使用不可变列表替代公有数组
public static final List<Thing> VALUES =
    Collections.unmodifiableList(Arrays.asList(PRIVATE_VALUES));

// 或者返回私有数组的拷贝
private static final Thing[] PRIVATE_VALUES = { ... };
public static final Thing[] values() {
    return PRIVATE_VALUES.clone();
}
```

> **复习提示**：受保护成员（protected）是类的导出API的一部分，必须永远支持。公有类中不应包含公有可变域。

---

### 条款16：在公有类中使用访问方法而非公有域

#### 退化类的问题

- **退化类（Degenerate classes）**：只有数据域没有行为的类，没有封装的好处
- 正确做法：包含**私有域**和**公有访问方法（getter/setter）**

```java
// 退化类（不推荐）
class Point {
    public double x;
    public double y;
}

// 正确做法
class Point {
    private double x;
    private double y;
    
    public double getX() { return x; }
    public double getY() { return y; }
    public void setX(double x) { this.x = x; }
    public void setY(double y) { this.y = y; }
}
```

#### 例外情况

| 场景 | 是否可以直接暴露数据域 |
|------|------------------------|
| **包级私有类** | ✅ 可以 |
| **私有嵌套类** | ✅ 可以 |
| **公有类** | ❌ 必须使用访问方法 |
| 公有类中的不可变域 | ⚠️ 危害较小，但仍不推荐 |

> **复习提示**：如果类可以在包外访问，就提供访问方法；如果是包级私有或私有嵌套类，直接暴露数据域是可以接受的。

---

### 条款17：使可变性最小化

#### 不可变类

**不可变类（Immutable Class）**：实例不能被修改的类。

常见示例：**`String`**、基本类型包装类（`Integer`、`Long`、`Boolean`等）

#### 如何使类成为不可变

1. **不提供修改状态的方法**（无 setter）
2. **保证类不会被扩展** —— 声明为 `final` 或使用**私有构造器**
3. **使所有域都为 `final`**
4. **使所有域都为 `private`**
5. **确保对任何可变组件的互斥访问** —— 防御性拷贝（defensive copies）

```java
// 不可变复数类完整示例
public final class Complex {
    private final double re;
    private final double im;
    
    public Complex(double re, double im) {
        this.re = re;
        this.im = im;
    }
    
    // 无 setter 方法
    public double realPart() { return re; }
    public double imaginaryPart() { return im; }
    
    // 函数式方法：返回新对象，不修改原对象
    public Complex plus(Complex c) {
        return new Complex(re + c.re, im + c.im);
    }
    
    public Complex minus(Complex c) {
        return new Complex(re - c.re, im - c.im);
    }
    
    public Complex times(Complex c) {
        return new Complex(re * c.re - im * c.im,
                           re * c.im + im * c.re);
    }
    
    public Complex dividedBy(Complex c) {
        double tmp = c.re * c.re + c.im * c.im;
        return new Complex((re * c.re + im * c.im) / tmp,
                           (im * c.re - re * c.im) / tmp);
    }
    
    @Override public boolean equals(Object o) { /* ... */ }
    @Override public int hashCode() { /* ... */ }
    @Override public String toString() { /* ... */ }
}
```

#### 函数式方法 vs 命令式方法

| | **函数式方法（Functional）** | **命令式方法（Imperative/Procedural）** |
|--|------------------------------|----------------------------------------|
| 操作结果 | 返回新对象，原对象不变 | 修改对象自身状态 |
| 示例 | `Complex c3 = c1.plus(c2);` | `c1.add(c2);` // c1 被修改 |

#### 不可变类的优缺点

**优点**：
- **简单** —— 只有一种状态
- **线程安全** —— 无需同步
- **可自由共享** —— 可以安全地复用实例
- **可共享内部信息** —— `String.substring()` 共享内部字符数组

**缺点**：
- 不同值需要不同对象 → 性能开销
- **解决方案**：提供**可变配套类**（如 `String` → `StringBuilder`）

> **复习提示**：除非有很好的理由让类可变，否则应该使类不可变。如果类不能做成不可变的，也要尽可能限制其可变性。

---

### 条款18：复合优先于继承

#### 何时使用继承

- 包内部的继承（安全的，同一个程序员控制）
- 专门为继承而设计并文档化的类

#### 为何避免继承

- **继承打破了封装性（encapsulation）**
- 子类依赖于父类的实现细节，父类变化可能导致子类异常

#### InstrumentedHashSet 问题示例

```java
// 问题：继承 HashSet 来统计添加元素次数
public class InstrumentedHashSet<E> extends HashSet<E> {
    private int addCount = 0;
    
    @Override public boolean add(E e) {
        addCount++;
        return super.add(e);
    }
    
    @Override public boolean addAll(Collection<? extends E> c) {
        addCount += c.size();  // 期望增加 c.size()
        return super.addAll(c);
    }
    
    public int getAddCount() { return addCount; }
}

// 问题：addAll 内部调用了 add，导致每个元素被计数两次！
// HashSet.addAll() → 每个元素调用 add() → addCount 被加了两次
```

#### 复合（Composition）的正确做法

```java
// 包装类（Wrapper Class）/ 转发类（Forwarding Class）
public class ForwardingSet<E> implements Set<E> {
    private final Set<E> s;
    public ForwardingSet(Set<E> s) { this.s = s; }
    
    public void clear() { s.clear(); }
    public boolean contains(Object o) { return s.contains(o); }
    public boolean add(E e) { return s.add(e); }
    public boolean addAll(Collection<? extends E> c) { return s.addAll(c); }
    // ... 转发所有方法
    public int size() { return s.size(); }
    public boolean isEmpty() { return s.isEmpty(); }
    // ...
}

// 装饰器：在转发基础上添加功能
public class InstrumentedSet<E> extends ForwardingSet<E> {
    private int addCount = 0;
    
    public InstrumentedSet(Set<E> s) { super(s); }
    
    @Override public boolean add(E e) {
        addCount++;
        return super.add(e);
    }
    
    @Override public boolean addAll(Collection<? extends E> c) {
        addCount += c.size();
        return super.addAll(c);
    }
    
    public int getAddCount() { return addCount; }
}
```

> **复习提示**：这被称为**包装类模式（Decorator Pattern）**。复合不依赖被包装类的实现细节，不存在继承的脆弱性问题。`InstrumentedSet` 可以用于任何 `Set` 实现（`HashSet`、`TreeSet` 等）。

---

### 条款20：接口优于抽象类

#### 接口 vs 抽象类

| 特性 | **接口** | **抽象类** |
|------|----------|------------|
| 多重实现 | ✅ 类可实现多个接口 | ❌ 只能继承一个抽象类 |
| 现有类更新 | ✅ 容易添加新接口 | ❌ 难以插入抽象类 |
| Mixin支持 | ✅ 理想的mixin定义方式 | ❌ 不适合 |
| 非层次结构 | ✅ 可组合多种行为 | ❌ 强制层次结构 |
| 骨架实现 | 可与抽象类结合 | 天然支持 |

#### 接口的优势

1. **现有类容易被更新以实现新接口**
2. **接口是定义mixin（混合类型）的理想选择** —— 如 `Comparable`
3. **接口允许构造非层次结构的类型框架**

```java
// 非层次结构：使用接口组合行为
public interface Singer { AudioClip sing(Song s); }
public interface Songwriter { Song compose(int chartPosition); }

// 可同时实现多个接口
public interface SingerSongwriter extends Singer, Songwriter {
    AudioClip strum();
    void actSensitive();
}
```

#### 骨架实现（Skeletal Implementation）

结合接口和抽象类的优点：
- **接口**定义类型（可多重实现）
- **抽象类**提供骨架实现（减少实现工作量）

```java
// 骨架实现类命名惯例：Abstract + 接口名
public abstract class AbstractMapEntry<K,V> implements Map.Entry<K,V> {
    // 必须实现的抽象方法
    public abstract K getKey();
    public abstract V getValue();
    
    // 提供默认实现
    public V setValue(V value) {
        throw new UnsupportedOperationException();
    }
    
    @Override public boolean equals(Object o) { /* ... */ }
    @Override public int hashCode() { /* ... */ }
    @Override public String toString() { /* ... */ }
}
```

> **复习提示**：骨架实现类命名惯例为 `AbstractInterfaceName`。这种方式称为**模拟多重继承**，类继承骨架实现同时可实现其他接口。

---

### 条款21：为后代设计接口

- **Java 8** 引入**缺省方法（default method）**
- 接口一旦发布就被广泛使用，**无法删除方法**或**修改已有方法签名**
- 缺省方法虽然方便，但**需谨慎设计**

#### SynchronizedCollection 的 removeIf 问题

```java
// Java 8 在 Collection 接口中添加了缺省方法 removeIf
// SynchronizedCollection 依赖于外部同步
// 但缺省 removeIf 实现未进行同步 → 线程安全问题
```

> **复习提示**：接口设计应经过仔细推敲和全面测试。接口一旦发布，修改的成本极高。

---

### 条款22：接口只用于定义类型

#### 常量接口（Constant Interface）—— 不推荐

```java
// 反模式：常量接口（不要这样做！）
public interface PhysicalConstants {
    static final double AVOGADROS_NUMBER = 6.022e23;
    static final double BOLTZMANN_CONSTANT = 1.38e-23;
    static final double ELECTRON_MASS = 9.11e-31;
}
```

常量接口的问题：
1. **泄露实现细节** —— 常量通常是实现细节
2. **污染命名空间** —— 实现类的命名空间被大量常量污染
3. **无法保证后续版本兼容** —— 若不再需要这些常量，仍需实现接口

#### 正确替代方案

```java
// 方案1：工具类 + 静态导入
public class PhysicalConstants {
    private PhysicalConstants() {} // 防止实例化
    
    public static final double AVOGADROS_NUMBER = 6.022e23;
    public static final double BOLTZMANN_CONSTANT = 1.38e-23;
    public static final double ELECTRON_MASS = 9.11e-31;
}

// 使用时：import static PhysicalConstants.*;
```

> **复习提示**：接口应该只用于定义类型，不应该用于导出常量。常量应放在合适的类或枚举中。

---

### 条款23：类层次优于标签类

#### 标签类（Tagged Class）—— 冗长且易出错

```java
// 标签类：用标签字段表示不同的变体
class Figure {
    enum Shape { RECTANGLE, CIRCLE };
    
    final Shape shape;  // 标签字段
    
    // 矩形专用字段
    double length;
    double width;
    
    // 圆形专用字段
    double radius;
    
    Figure(double radius) {  // 圆形构造器
        shape = Shape.CIRCLE;
        this.radius = radius;
    }
    
    Figure(double length, double width) {  // 矩形构造器
        shape = Shape.RECTANGLE;
        this.length = length;
        this.width = width;
    }
    
    double area() {
        switch(shape) {  // 处处需要条件判断
            case RECTANGLE: return length * width;
            case CIRCLE: return Math.PI * radius * radius;
            default: throw new AssertionError();
        }
    }
}
```

标签类的问题：
- **冗长** —— 多个变体的代码混在一起
- **易出错** —— 容易忘记处理某个标签
- **效率低下** —— 实例包含所有变体的字段

#### 类层次（Class Hierarchy）—— 正确做法

```java
// 抽象基类定义共同行为
abstract class Figure {
    abstract double area();
}

// 每个变体一个子类
class Circle extends Figure {
    final double radius;
    Circle(double radius) { this.radius = radius; }
    @Override double area() { return Math.PI * radius * radius; }
}

class Rectangle extends Figure {
    final double length;
    final double width;
    Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }
    @Override double area() { return length * width; }
}
```

优点：
- 代码**清晰简洁**
- 没有不相关的数据域
- **不必维护条件语句**（消除 switch）

> **复习提示**：标签类是类层次的拙劣模仿。遇到标签类时，应考虑重构为类层次结构。

---

### 条款24：优先考虑静态成员类

#### 嵌套类（Nested Class）的分类

1. **静态成员类（static member class）**
2. **非静态成员类（non-static member class / inner class）**
3. **匿名类（anonymous class）**
4. **局部类（local class）**

#### 静态成员类

- 可在实例之外**独立存在**
- 最常见用途：作为公有的辅助类（如 `Calculator.Operation.PLUS`）
- 如果声明成员类不需要访问外部实例，就**始终加上 `static`**

#### 非静态成员类（内部类）

- 每个实例都隐含地关联一个外部类实例
- 有额外的内存消耗和构造开销
- 常见用途：**适配器模式**（如 `Map` 的 `keySet()`、`values()`、`entrySet()` 返回的集合视图）

#### 匿名类

- **同时声明和实例化**
- 无名字、无静态成员
- 使用场景：函数对象（如 `Comparator`）、过程对象、`Runnable` 等
- 应保持**简短**（< 10行），否则可读性差

```java
// 匿名类示例
Collections.sort(list, new Comparator<String>() {
    @Override
    public int compare(String s1, String s2) {
        return s1.length() - s2.length();
    }
});
```

#### 局部类

- 有名字，可**重复使用**
- 可在方法内任意位置声明
- 几乎不会使用

> **复习提示**：优先选择**静态成员类**。只有必须访问外部实例时，才使用非静态成员类。

---

### 条款25：限制源文件为单个顶级类

- 单个源文件定义多个顶级类存在**风险**
- **编译结果受文件传给编译器的顺序影响** —— 可能产生不同的编译输出

```java
// 不要这样做：Main.java 中定义两个类
class Main {
    public static void main(String[] args) {
        System.out.println(Utensil.NAME + Dessert.NAME);
    }
}

// 同一个文件中的另一个顶级类
class Utensil {
    static final String NAME = "pan";
}

class Dessert {
    static final String NAME = "cake";
}
```

#### 解决方案

| 方案 | 做法 |
|------|------|
| **推荐** | 每个顶级类放入**单独的文件**（`Utensil.java`、`Dessert.java`） |
| 替代 | 使用**静态成员类**将相关类组织在一起 |

> **复习提示**：永远不要把多个顶级类或接口放到一个源文件中。这可能导致编译错误和行为不一致。

---

## 第5章：泛型

> **复习要点**：泛型的核心目标是**编译时类型安全**，消除 `ClassCastException`。重点掌握**PECS原则**、**类型擦除**、**通配符**等概念。

---

### 泛型基础

#### 为什么引入泛型

- 与 **C++ template** 类似但目的有区别
- **减少程序运行错误** —— 编译时类型检查
- **减少方法的重载**

```java
// 原始类型（raw type）：运行时才报错
Box box = new Box();
box.set("abc");
Integer a = (Integer) box.get(); // ClassCastException!

// 泛型：编译时就报错
Box<Integer> box = new Box<Integer>();
// box.set("abc");  // 编译错误！类型不匹配
Integer a = box.get(); // 无需强制转换
```

#### 命名规则

| 类型参数 | 含义 |
|----------|------|
| **E** | Element（元素） |
| **K** | Key（键） |
| **N** | Number（数字） |
| **T** | Type（类型） |
| **V** | Value（值） |
| **S, U, V** | 第2/3/4个类型参数 |

#### 多个类型变量

```java
public interface Pair<K, V> {
    public K getKey();
    public V getValue();
}

// 使用
Pair<String, Integer> p1 = new OrderedPair<>("Even", 8);
```

#### 泛型方法

```java
public static <K, V> boolean compare(Pair<K, V> p1, Pair<K, V> p2) {
    return p1.getKey().equals(p2.getKey()) &&
           p1.getValue().equals(p2.getValue());
}
```

#### 限制类型参数（Bounded Type Parameters）

```java
// 单边界：T 限定为 Number 的子类
class Box<T extends Number> { }

// 多边界：最多一个类，多个接口（类在前）
class Box<T extends Number & Cloneable & Comparable<T>> { }
```

#### 泛型类的继承

> **重要**：`Box<Integer>` **不是** `Box<Number>` 的子类型！

```java
Box<Integer> intBox = new Box<>();
// Box<Number> numBox = intBox; // 编译错误！
```

#### 类型推断

```java
// Java 7 钻石运算符（Diamond Operator）
Map<String, List<String>> myMap = new HashMap<>();

// 泛型方法也可推断
List<String> list = Collections.emptyList();
```

#### 通配符（Wildcards）

```java
// 上界通配符：接受 Box<Integer>, Box<Double> 等
public void boxTest(Box<? extends Number> n) { }

// 下界通配符
public void addNumbers(List<? super Integer> list) { }
```

#### 类型擦除（Type Erasure）

- 编译期间泛型类型信息被**擦除**
- `List<Object>` 和 `List<String>` 编译后都变为 `List`
- 泛型只在编译期存在，运行时不保留类型参数信息

```java
// 编译前
List<String> strList = new ArrayList<>();
List<Integer> intList = new ArrayList<>();

// 编译后（两者类型相同）
List strList = new ArrayList();
List intList = new ArrayList();
```

---

### 条款26：不要使用原始类型

- **原始类型（raw type）**：不带类型参数的泛型名称，如 `List`（而非 `List<String>`）
- 使用原始类型会失去**类型安全性**，可能导致运行时 `ClassCastException`

```java
// 错误：使用原始类型
List list = new ArrayList();
list.add("hello");
list.add(42);     // 编译通过，运行时报错
String s = (String) list.get(1); // ClassCastException!

// 正确：使用泛型
List<String> list = new ArrayList<>();
list.add("hello");
// list.add(42); // 编译错误！
```

#### `List` vs `List<Object>`

| | `List`（原始类型） | `List<Object>` |
|--|--------------------|----------------|
| 类型安全 | ❌ 逃避泛型检查 | ✅ 有类型检查 |
| 可添加任意类型 | ✅ | ✅ |
| 类型参数信息 | 无 | 明确为 Object |

#### 无限制通配符 `Set<?>`

- **`Set<?>`** 是**安全的** —— 只能读取，不能写入（null 除外）
- 用于表示"某种类型的 Set"，但不知道具体是什么类型

```java
// 正确：无限制通配符是类型安全的
static int numElementsInCommon(Set<?> s1, Set<?> s2) { ... }
```

#### 例外情况（允许使用原始类型）

1. **类文字（class literal）**：`List.class`、`String[].class`（不允许 `List<String>.class`）
2. **`instanceof` 运算符**：

```java
if (o instanceof Set) {        // 原始类型
    Set<?> s = (Set<?>) o;     // 通配符类型转换
    // ...
}
```

> **复习提示**：一旦使用了原始类型，就会失去泛型的所有安全性和表达性优势。唯一的例外是类文字和 `instanceof`。

---

### 条款27：消除非受检警告

- 尽可能**改写代码**消除非受检（unchecked）警告
- 如果无法消除，使用 **`@SuppressWarnings("unchecked")`**

```java
// 正确使用 @SuppressWarnings
@SuppressWarnings("unchecked")
public <T> T[] toArray(T[] a) {
    if (a.length < size) {
        // 安全原因说明：a 是类型 T 的数组，
        // elements 只包含 T 类型元素
        return (T[]) Arrays.copyOf(elements, size, a.getClass());
    }
    // ...
}
```

使用规则：
1. 在**最小范围**使用（变量声明、短方法）
2. 必须添加**注释说明为什么安全**
3. 不要在整个类上随意使用

> **复习提示**：每当你使用 `@SuppressWarnings("unchecked")` 注解时，都要添加一条注释，说明为什么这么做是安全的。

---

### 条款28：列表优先于数组

#### 数组 vs 泛型列表的关键区别

| 特性 | **数组** | **泛型列表** |
|------|----------|--------------|
| 协变性（Covariance） | ✅ `Integer[]` 是 `Object[]` 的子类型 | ❌ `List<Integer>` 不是 `List<Object>` 的子类型 |
| 具体化（Reification） | ✅ 运行时知道元素类型 | ❌ 擦除（erasure），运行时不知道 |
| 类型安全 | ❌ 运行时才报错 | ✅ 编译时报错 |

#### 数组的协变问题

```java
// 数组是协变的：编译通过，运行时报错
Object[] objArray = new Long[10];
objArray[0] = "hello"; // ArrayStoreException！

// 泛型是不可变的：编译时就报错
// List<Object> objList = new List<Long>(); // 编译错误！
// objList.add("hello"); // 不会执行到这里
```

#### 无法创建泛型数组

```java
// 非法：无法创建泛型数组
// List<String>[] stringLists = new List<String>[1]; // 编译错误！

// 原因：数组的协变 + 泛型的不可变 = 类型系统漏洞
// 若允许，则可构造出运行时 ClassCastException
```

#### Chooser 类示例

```java
// 错误做法：使用数组
public class Chooser<T> {
    private final T[] choiceArray;
    
    public Chooser(Collection<T> choices) {
        choiceArray = (T[]) choices.toArray(); // 非受检转换
    }
    
    public T choose() {
        Random rnd = ThreadLocalRandom.current();
        return choiceArray[rnd.nextInt(choiceArray.length)];
    }
}

// 正确做法：使用列表
public class Chooser<T> {
    private final List<T> choiceList;
    
    public Chooser(Collection<T> choices) {
        choiceList = new ArrayList<>(choices); // 安全
    }
    
    public T choose() {
        Random rnd = ThreadLocalRandom.current();
        return choiceList.get(rnd.nextInt(choiceList.size()));
    }
}
```

> **复习提示**：数组和泛型不能很好地混用。如果得到编译错误或警告，第一反应应该是用列表（`List`）替代数组（`T[]`）。

---

### 条款29：优先考虑泛型

#### 将类泛型化

示例：将基于 Object 的 Stack 改为泛型 Stack

```java
// 方法1：创建 Object 数组，转换为泛型数组类型
public class Stack<E> {
    private E[] elements;
    private int size = 0;
    private static final int DEFAULT_INITIAL_CAPACITY = 16;
    
    @SuppressWarnings("unchecked")
    public Stack() {
        // 无法直接创建 E[]，需要强制转换
        elements = (E[]) new Object[DEFAULT_INITIAL_CAPACITY];
    }
    
    public void push(E e) {
        ensureCapacity();
        elements[size++] = e;
    }
    
    public E pop() {
        if (size == 0) throw new EmptyStackException();
        E result = elements[--size];
        elements[size] = null; // 防止内存泄漏
        return result;
    }
}
```

```java
// 方法2：elements 域类型改为 Object[]，获取时类型转换
public class Stack<E> {
    private Object[] elements;
    private int size = 0;
    
    public Stack() {
        elements = new Object[DEFAULT_INITIAL_CAPACITY]; // 合法
    }
    
    public E pop() {
        if (size == 0) throw new EmptyStackException();
        // 类型转换（push 只接受 E 类型，所以安全）
        @SuppressWarnings("unchecked")
        E result = (E) elements[--size];
        elements[size] = null;
        return result;
    }
}
```

> **复习提示**：方法1只需一次转换（构造器中），方法2每次取元素都需转换。通常**方法1更可取**，性能稍好。两种方法都需要 `@SuppressWarnings` 和注释。

---

### 条款30：优先考虑泛型方法

#### 泛型方法示例

```java
// 泛型方法 union
public static <E> Set<E> union(Set<E> s1, Set<E> s2) {
    Set<E> result = new HashSet<>(s1);
    result.addAll(s2);
    return result;
}
```

#### 泛型单例工厂（Generic Singleton Factory）

```java
// 不可变对象的泛型单例
public static <T> List<T> emptyList() {
    return (List<T>) EMPTY_LIST;
}
```

#### 递归类型限制（Recursive Type Bound）

```java
// E 必须是 Comparable<E> 的子类型（E 可与自身比较）
public static <E extends Comparable<E>> E max(Collection<E> c) {
    if (c.isEmpty()) throw new IllegalArgumentException("Empty collection");
    
    E result = null;
    for (E e : c)
        if (result == null || e.compareTo(result) > 0)
            result = e;
    return result;
}
```

> **复习提示**：递归类型限制常用于 `Comparable` 接口。`<E extends Comparable<E>>` 表示 E 可以与同类型的 E 比较。

---

### 条款31：利用有限制的通配符来提升API的灵活性

#### PECS 原则

> **PECS**：**Producer-Extends, Consumer-Super**

- **生产者（Producer）**使用 `extends` —— 只从中**读取**数据
- **消费者（Consumer）**使用 `super` —— 只向其中**写入**数据

```java
public class Stack<E> {
    // pushAll：src 是生产者（产生 E 供 Stack 使用）
    public void pushAll(Iterable<? extends E> src) {
        for (E e : src)
            push(e);
    }
    
    // popAll：dst 是消费者（接收从 Stack 弹出的 E）
    public void popAll(Collection<? super E> dst) {
        while (!isEmpty())
            dst.add(pop());
    }
}
```

#### swap 方法中的通配符捕获

```java
// 辅助方法捕获通配符类型
public static void swap(List<?> list, int i, int j) {
    swapHelper(list, i, j);
}

// 私有辅助方法捕获类型参数
private static <E> void swapHelper(List<E> list, int i, int j) {
    list.set(i, list.set(j, list.get(i)));
}
```

> **复习提示**：对于 `Comparable` 和 `Comparator`，也遵循 PECS：`Comparable<? super T>` 优于 `Comparable<T>`，因为前者允许 T 与父类比较。

---

### 条款33：优先考虑类型安全的异构容器

#### 问题

普通泛型容器（如 `Map<K, V>`）中键和值的类型在容器创建时固定，灵活性受限。

#### 解决方案

将**键（key）参数化**而非容器本身。

```java
// 类型安全的异构容器
public class Favorites {
    // 键是 Class<?>（参数化的），值是 Object
    private Map<Class<?>, Object> favorites = new HashMap<>();
    
    // putFavorite：将键参数化
    public <T> void putFavorite(Class<T> type, T instance) {
        favorites.put(Objects.requireNonNull(type), instance);
    }
    
    // getFavorite：使用动态类型转换
    public <T> T getFavorite(Class<T> type) {
        return type.cast(favorites.get(type));
    }
}

// 使用
Favorites f = new Favorites();
f.putFavorite(String.class, "Java");
f.putFavorite(Integer.class, 0xcafebabe);
f.putFavorite(Class.class, Favorites.class);

String s = f.getFavorite(String.class);     // "Java"
int i = f.getFavorite(Integer.class);        // 0xcafebabe
Class<?> c = f.getFavorite(Class.class);     // Favorites.class
```

> **复习提示**：`Favorites` 实例是**类型安全的**（get 自动返回正确类型）、**异构的**（可存任意类型）。这是通过 **`Class` 对象作为键** + **`Class.cast()` 方法**实现的。 limitations 在于不能存放不可具体化的类型（如 `List<String>`）。

---

## 综合复习要点总结

### 第4章核心原则

| 条款 | 核心要点 |
|------|----------|
| 15 | **最小化可访问性**：private > package-private > protected > public |
| 16 | 公有类使用 getter/setter，**不要暴露公有域** |
| 17 | **使类不可变**（final fields, no mutators, defensive copies） |
| 18 | **复合优先于继承**，使用包装类模式避免封装性被破坏 |
| 20 | **接口优于抽象类**，骨架实现结合两者优点 |
| 21 | 谨慎设计接口，接口一旦发布难以修改 |
| 22 | 接口只用于**定义类型**，不用作常量导出 |
| 23 | **类层次优于标签类**，消除 switch/条件判断 |
| 24 | 优先使用**静态成员类** |
| 25 | 一个源文件**只放一个顶级类** |

### 第5章核心原则

| 条款 | 核心要点 |
|------|----------|
| 26 | **不要使用原始类型**（raw type），用泛型或无界通配符 |
| 27 | 消除非受检警告，`@SuppressWarnings` 要在最小范围使用 |
| 28 | **列表优先于数组**，数组协变+具体化与泛型不兼容 |
| 29 | 将 API 泛型化，提高类型安全性 |
| 30 | 优先使用泛型方法 + PECS 原则 |
| 31 | **PECS**：Producer-Extends, Consumer-Super |
| 33 | 类型安全的异构容器：将**键参数化** |

### 高频考点

1. **信息隐藏的好处**（条款15）
2. **不可变类的5条规则** + 优缺点（条款17）
3. **InstrumentedHashSet 问题** + 复合/包装类解决方案（条款18）
4. **接口 vs 抽象类** + 骨架实现（条款20）
5. **数组协变 vs 泛型不可变** + 为什么不能用泛型数组（条款28）
6. **PECS 原则** + pushAll/popAll 的通配符选择（条款31）
7. **Favorites 类**的设计思路（条款33）


---

## 第6章 枚举和注解

### 条款34：用 enum 代替 int 常量

#### int 枚举模式的缺点

- **类型安全性不足**：int 常量不具备类型检查，可将不同含义的 int 值混用
- **程序脆弱**：int 值编译到客户端中，后续修改值需重新编译客户端
- **打印不方便**：输出的是数字，不具可读性
- 需要为每个常量提供命名前缀作为命名空间（如 `APPLE_FUJI`、`ORANGE_NAVEL`）

#### String 枚举模式

- **性能问题**：依赖字符串比较，效率低
- **硬编码容易出错**：字符串拼写错误在编译期无法发现
- 可能导致字符串常量占用不必要的内存

#### 枚举类型的优势

Java 的 `enum` 是**完整的类**，编译器自动为每个枚举导出 `public static final` 字段。

```java
public enum Apple { FUJI, PIPPIN, GRANNY_SMITH }
public enum Orange { NAVEL, TEMPLE, BLOOD }
```

枚举类型的核心优势：
- **编译时类型安全**：无法将 `Apple` 类型与 `Orange` 类型混用
- **命名空间隔离**：不同枚举类型的常量名称不会冲突
- **可添加方法和域**：枚举是类，可以拥有字段、方法、构造函数
- **自动提供 `toString()`**：打印友好的名称
- **内置 `valueOf(String)`**：实现字符串到枚举的转换
- **内置 `values()`**：获取所有常量数组

#### 带数据和行为的枚举示例（Planet）

```java
public enum Planet {
    MERCURY(3.302e+23, 2.439e6),
    VENUS(4.869e+24, 6.052e6),
    EARTH(5.975e+24, 6.378e6),
    MARS(6.419e+23, 3.393e6),
    JUPITER(1.899e+27, 7.149e7),
    SATURN(5.685e+26, 6.027e7),
    URANUS(8.683e+25, 2.556e7),
    NEPTUNE(1.024e+26, 2.477e7);

    private final double mass;           // 质量（千克）
    private final double radius;         // 半径（米）
    private final double surfaceGravity; // 表面重力

    // 常量特定的数据 + 通用计算
    private static final double G = 6.67300E-11;

    Planet(double mass, double radius) {
        this.mass = mass;
        this.radius = radius;
        this.surfaceGravity = G * mass / (radius * radius);
    }

    public double mass() { return mass; }
    public double radius() { return radius; }
    public double surfaceGravity() { return surfaceGravity; }

    // 行为方法
    public double surfaceWeight(double mass) {
        return mass * surfaceGravity; // F = ma
    }
}
```

> **复习要点**：枚举构造函数默认是 `private`，无需显式声明。枚举常量列表必须是第一个元素，以分号结尾后才能声明字段和方法。

#### 特定于常量的方法实现

**方式一：switch 语句（不推荐）**

```java
public enum Operation {
    PLUS, MINUS, TIMES, DIVIDE;

    public double apply(double x, double y) {
        switch (this) {
            case PLUS:  return x + y;
            case MINUS: return x - y;
            case TIMES: return x * y;
            case DIVIDE: return x / y;
        }
        throw new AssertionError("Unknown op: " + this);
    }
}
```n
> **注意**：switch 方式的问题是添加新常量时容易遗漏对应的 case，编译器不会报错。

**方式二：特定于常量的方法实现（推荐）**

```java
public enum Operation {
    PLUS("+") {
        public double apply(double x, double y) { return x + y; }
    },
    MINUS("-") {
        public double apply(double x, double y) { return x - y; }
    },
    TIMES("*") {
        public double apply(double x, double y) { return x * y; }
    },
    DIVIDE("/") {
        public double apply(double x, double y) { return x / y; }
    };

    private final String symbol;

    Operation(String symbol) { this.symbol = symbol; }

    @Override public String toString() { return symbol; }

    public abstract double apply(double x, double y);
}
```

> **复习要点**：每个枚举常量可以拥有自己特定的实现（类似匿名子类），通过声明抽象方法强制每个常量提供实现。添加新常量时必须实现抽象方法，编译器会检查。

#### fromString 方法实现

使用**静态 Map** 缓存字符串到枚举的映射，实现高效查找：

```java
public enum Operation {
    PLUS("+"), MINUS("-"), TIMES("*"), DIVIDE("/");

    private final String symbol;

    // 静态 Map 缓存，实现字符串到枚举的反向查找
    private static final Map<String, Operation> stringToEnum =
        Stream.of(values()).collect(
            toMap(Object::toString, e -> e));

    Operation(String symbol) { this.symbol = symbol; }

    // 根据字符串查找对应的枚举常量
    public static Optional<Operation> fromString(String symbol) {
        return Optional.ofNullable(stringToEnum.get(symbol));
    }
}
```

> **复习要点**：`Optional` 的返回值比返回 `null` 更安全，调用方必须显式处理值不存在的情况。

#### 策略枚举（Strategy Enum）

当多个枚举常量需要**共享代码**时，使用**策略枚举**模式解决代码重复问题。

```java
enum PayrollDay {
    MONDAY(WEEKDAY), TUESDAY(WEEKDAY), WEDNESDAY(WEEKDAY),
    THURSDAY(WEEKDAY), FRIDAY(WEEKDAY),
    SATURDAY(WEEKEND), SUNDAY(WEEKEND);

    private final PayType payType;

    PayrollDay(PayType payType) { this.payType = payType; }

    int pay(int minutesWorked, int payRate) {
        return payType.pay(minutesWorked, payRate);
    }

    // 策略枚举：将工资计算逻辑封装为独立枚举
    enum PayType {
        WEEKDAY {
            int overtimePay(int mins, int payRate) {
                return mins <= MINS_PER_SHIFT ? 0 :
                    (mins - MINS_PER_SHIFT) * payRate / 2;
            }
        },
        WEEKEND {
            int overtimePay(int mins, int payRate) {
                return mins * payRate / 2;
            }
        };

        abstract int overtimePay(int mins, int payRate);
        private static final int MINS_PER_SHIFT = 8 * 60;

        int pay(int minsWorked, int payRate) {
            int basePay = minsWorked * payRate;
            return basePay + overtimePay(minsWorked, payRate);
        }
    }
}
```

> **复习要点**：策略枚举将变体行为提取到独立的嵌套枚举中，主枚举通过组合方式引用策略，避免大量重复代码。当枚举本身无法表达某种行为时，也可以用 switch 语句作为备选方案。

---

### 条款35：用实例域代替序数

**绝对不要**使用 `ordinal()` 方法来导出与枚举常量关联的值。

```java
// 错误做法：依赖 ordinal()
public enum Ensemble {
    SOLO, DUET, TRIO, QUARTET, QUINTET,
    SEXTET, SEPTET, OCTET, NONET, DECTET;

    public int numberOfMusicians() { return ordinal() + 1; } // 危险！
}
```

**正确做法**：使用**实例域**存储关联值。

```java
public enum Ensemble {
    SOLO(1), DUET(2), TRIO(3), QUARTET(4), QUINTET(5),
    SEXTET(6), SEPTET(7), OCTET(8), DOUBLE_QUARTET(8),
    NONET(9), DECTET(10), TRIPLE_QUARTET(12);

    private final int numberOfMusicians;

    Ensemble(int size) { this.numberOfMusicians = size; }

    public int numberOfMusicians() { return numberOfMusicians; }
}
```

> **复习要点**：
> - `ordinal()` 返回枚举常量在声明中的位置（从 0 开始），一旦常量顺序调整就会出错
> - 实例域方式允许值与声明顺序**不一致**（如 `DOUBLE_QUARTET(8)`、`TRIPLE_QUARTET(12)`）
> - `EnumSet`、`EnumMap` 内部使用 `ordinal()`，但这是框架的实现细节，不应在应用代码中使用

---

### 条款36：用 EnumSet 代替位域

**位域（bit field）**的缺点：
- 不具类型安全性，int 值可以任意组合
- 不具可读性，调试困难
- 无法遍历所有"设置"的位
- 需要手动位运算操作

```java
// 旧做法：位域（bit field）—— 不推荐
public class Text {
    public static final int STYLE_BOLD      = 1 << 0;  // 1
    public static final int STYLE_ITALIC    = 1 << 1;  // 2
    public static final int STYLE_UNDERLINE = 1 << 2;  // 4
    public static final int STYLE_STRIKETHROUGH = 1 << 3;  // 8

    public void applyStyles(int styles) { ... } // 参数类型只是 int
}

// 使用
text.applyStyles(STYLE_BOLD | STYLE_ITALIC);
```

**正确做法：EnumSet**

```java
public class Text {
    public enum Style { BOLD, ITALIC, UNDERLINE, STRIKETHROUGH }

    // 参数类型是 Set<Style>，任何 Set 实现均可传入
    public void applyStyles(Set<Style> styles) { ... }
}

// 使用
text.applyStyles(EnumSet.of(Style.BOLD, Style.ITALIC));
```

> **复习要点**：
> - `EnumSet` 在内部使用**位向量**实现，性能与位域相当
> - 接受 `Set<Style>` 而非 `EnumSet<Style>` 作为参数，提高灵活性
> - `EnumSet.of()` 可以传入 1~5 个常量，超过5个可用 `EnumSet.allOf()` 或 `EnumSet.copyOf()`

---

### 条款37：用 EnumMap 代替序数索引

**绝对不要**使用 `ordinal()` 来索引数组。

```java
// 错误做法：使用 ordinal() 索引数组
Plant[] garden = ...;
Set<Plant>[] plantsByLifeCycle = (Set<Plant>[]) new Set[Plant.LifeCycle.values().length];
for (int i = 0; i < plantsByLifeCycle.length; i++)
    plantsByLifeCycle[i] = new HashSet<>();
for (Plant p : garden)
    plantsByLifeCycle[p.lifeCycle.ordinal()].add(p);
```

**正确做法：EnumMap**

```java
Map<Plant.LifeCycle, Set<Plant>> plantsByLifeCycle =
    new EnumMap<>(Plant.LifeCycle.class);
for (Plant.LifeCycle lc : Plant.LifeCycle.values())
    plantsByLifeCycle.put(lc, new HashSet<>());
for (Plant p : garden)
    plantsByLifeCycle.get(p.lifeCycle).add(p);
```

> **复习要点**：
> - `EnumMap` 内部将枚举的 `ordinal()` 用作数组索引，但封装了这一细节
> - **类型安全**：键类型在编译期被限定为特定枚举
> - 无需手动维护数组大小与枚举常量数量的同步关系
> - 比 `HashMap` 更快，因为不需要哈希计算

#### 嵌套 EnumMap 处理二维关系

```java
public enum Phase {
    SOLID, LIQUID, GAS;

    public enum Transition {
        MELT(SOLID, LIQUID),    FREEZE(LIQUID, SOLID),
        BOIL(LIQUID, GAS),      CONDENSE(GAS, LIQUID),
        SUBLIME(SOLID, GAS),    DEPOSIT(GAS, SOLID);

        private final Phase from;
        private final Phase to;

        Transition(Phase from, Phase to) {
            this.from = from;
            this.to = to;
        }

        // 初始化嵌套 EnumMap：从状态 -> (到状态 -> 转换)
        private static final Map<Phase, Map<Phase, Transition>> m =
            Stream.of(values()).collect(groupingBy(
                t -> t.from,
                () -> new EnumMap<>(Phase.class),
                toMap(t -> t.to, t -> t,
                    (x, y) -> y,  // 合并函数（不会发生）
                    () -> new EnumMap<>(Phase.class))));

        public static Transition from(Phase from, Phase to) {
            return m.get(from).get(to);
        }
    }
}
```

> **复习要点**：嵌套 `EnumMap` 可以优雅地表示**二维枚举关系**（如状态转换表）。添加新的 Phase 只需在枚举中新增常量并增加对应的 Transition 条目即可。

---

### 条款38：用接口模拟可伸缩的枚举

**枚举类型无法被继承**（编译器限制），但可以通过**实现接口**来模拟可扩展性。

```java
// 1. 定义操作接口
public interface Operation {
    double apply(double x, double y);
}

// 2. 基础枚举实现接口
public enum BasicOperation implements Operation {
    PLUS("+")  { public double apply(double x, double y) { return x + y; } },
    MINUS("-") { public double apply(double x, double y) { return x - y; } },
    TIMES("*") { public double apply(double x, double y) { return x * y; } },
    DIVIDE("/"){ public double apply(double x, double y) { return x / y; } };

    private final String symbol;
    BasicOperation(String symbol) { this.symbol = symbol; }
    @Override public String toString() { return symbol; }
}

// 3. 扩展枚举（实现同一接口）
public enum ExtendedOperation implements Operation {
    EXP("^") { public double apply(double x, double y) { return Math.pow(x, y); } },
    REMAINDER("%") { public double apply(double x, double y) { return x % y; } };

    private final String symbol;
    ExtendedOperation(String symbol) { this.symbol = symbol; }
    @Override public String toString() { return symbol; }
}
```

#### 泛型约束写法

```java
// 受限类型参数：同时是 Enum<T> 的子类且实现了 Operation 接口
private static <T extends Enum<T> & Operation> void test(
        Class<T> opEnumType, double x, double y) {
    for (Operation op : opEnumType.getEnumConstants())
        System.out.printf("%f %s %f = %f%n", x, op, y, op.apply(x, y));
}

// 或使用有限制的通配符类型
private static void test(Collection<? extends Operation> opSet,
                         double x, double y) {
    for (Operation op : opSet)
        System.out.printf("%f %s %f = %f%n", x, op, y, op.apply(x, y));
}
```

> **复习要点**：
> - `<T extends Enum<T> & Operation>` 是**多边界**的写法，类在前接口在后
> - API 设计时应优先采用**接口类型**而非具体实现类型作为参数
> - 虽然枚举不可继承，但通过接口可以实现"扩展枚举"的效果

---

### 条款39：注解优先于命名模式

#### 命名模式的缺点

- **拼写错误导致静默失败**：如将方法命名为 `tsetXX` 而非 `testXX`，测试框架会忽略
- **无法确保仅用于正确程序元素**：如在方法外误用了 `test` 前缀
- **缺乏配置参数**：命名模式无法携带元数据

#### 标记注解（Marker Annotation）

```java
// 定义测试注解
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Test {
}
```

| 元注解 | 作用 |
|--------|------|
| `@Retention(RUNTIME)` | 注解在运行时保留（可通过反射读取） |
| `@Target(METHOD)` | 限定注解只能用于方法 |

#### 带参数的注解

```java
// 单个异常参数
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface ExceptionTest {
    Class<? extends Throwable> value();
}

// 使用
@ExceptionTest(ArithmeticException.class)
public static void m1() { int i = 0; i = i / i; }  // 应抛出 ArithmeticException
```

#### 带数组参数的注解

```java
// 多个异常参数
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface ExceptionTest {
    Class<? extends Throwable>[] value();
}

// 使用：传入异常数组
@ExceptionTest({ IndexOutOfBoundsException.class, NullPointerException.class })
public static void doublyBad() {
    List<String> list = new ArrayList<>();
    list.addAll(5, null); // 可能抛出两种异常之一
}
```

#### 可重复注解（@Repeatable）

```java
// 1. 定义容器注解
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface ExceptionTestContainer {
    ExceptionTest[] value();
}

// 2. 在注解上标记 @Repeatable
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@Repeatable(ExceptionTestContainer.class)
public @interface ExceptionTest {
    Class<? extends Throwable> value();
}

// 3. 可重复使用同一个注解
@ExceptionTest(IndexOutOfBoundsException.class)
@ExceptionTest(NullPointerException.class)
public static void doublyBad() { ... }
```

#### 注解处理器（反射读取）

```java
public static void main(String[] args) throws Exception {
    int tests = 0;
    int passed = 0;
    Class<?> testClass = Class.forName(args[0]);
    for (Method m : testClass.getDeclaredMethods()) {
        if (m.isAnnotationPresent(Test.class)) {
            tests++;
            try {
                m.invoke(null);
                passed++;
            } catch (InvocationTargetException e) {
                System.out.println(m + " failed: " + e.getCause());
            } catch (Exception e) {
                System.out.println("Invalid @Test: " + m);
            }
        }
    }
    System.out.printf("Passed: %d, Failed: %d%n", passed, tests - passed);
}
```

> **复习要点**：
> - `@Retention` 有三个级别：`SOURCE`（编译期丢弃）、`CLASS`（默认，存于类文件但运行时不可见）、`RUNTIME`（运行时可通过反射获取）
> - `@Repeatable` 必须同时定义**容器注解**类型
> - 注解使得框架可以在编译期检查，避免命名模式的拼写问题

---
---

## 第7章 Lambda 和 Stream

### 条款42：Lambda 优先于匿名类

#### 函数接口（Functional Interface）

**函数接口**是指**带有单个抽象方法的接口**（可以有多个默认方法或静态方法）。

Java 标准函数接口：

| 接口 | 方法签名 | 用途 |
|------|---------|------|
| `Runnable` | `void run()` | 无参数无返回值 |
| `Comparator<T>` | `int compare(T, T)` | 比较两个对象 |
| `Callable<V>` | `V call()` | 无参数有返回值，可抛异常 |
| `ActionListener` | `void actionPerformed(ActionEvent)` | 事件处理 |

#### Lambda 表达式替代匿名类

```java
// 匿名类写法（冗长）
Collections.sort(words, new Comparator<String>() {
    public int compare(String s1, String s2) {
        return Integer.compare(s1.length(), s2.length());
    }
});

// Lambda 写法（简洁）
Collections.sort(words, (s1, s2) -> Integer.compare(s1.length(), s2.length()));

// 更简洁：方法引用
Collections.sort(words, Comparator.comparingInt(String::length));

// 最简洁：利用 List.sort 默认方法
words.sort(Comparator.comparingInt(String::length));
```

#### 在枚举中使用 Lambda

```java
public enum Operation {
    PLUS("+", (x, y) -> x + y),
    MINUS("-", (x, y) -> x - y),
    TIMES("*", (x, y) -> x * y),
    DIVIDE("/", (x, y) -> x / y);

    private final String symbol;
    private final DoubleBinaryOperator op;

    Operation(String symbol, DoubleBinaryOperator op) {
        this.symbol = symbol;
        this.op = op;
    }

    public double apply(double x, double y) {
        return op.applyAsDouble(x, y);
    }
}
```

> **复习要点**：
> - Lambda 的类型推导依赖于**上下文**（目标类型）
> - Lambda **没有 this 指向自身**，this 指向外部类
> - Lambda 不能用于**多个抽象方法**的接口（必须用匿名类）
> - Lambda 代码应**简短**，过长会降低可读性
> - Lambda 中无法获取自身引用，匿名类可以

---

### 条款43：方法引用优先于 Lambda

方法引用通常比 Lambda 表达式**更简洁、更具可读性**。

```java
// Lambda 写法
frequencyTable.merge(s, 1, (count, incr) -> count + incr);

// 方法引用写法（更简洁）
frequencyTable.merge(s, 1, Integer::sum);
```

方法引用的五种形式：

| 形式 | 示例 | 等效 Lambda |
|------|------|------------|
| 静态方法引用 | `Integer::parseInt` | `str -> Integer.parseInt(str)` |
| 实例方法引用（绑定） | `System.out::println` | `x -> System.out.println(x)` |
| 实例方法引用（非绑定） | `String::toLowerCase` | `str -> str.toLowerCase()` |
| 类构造器引用 | `TreeMap::new` | `() -> new TreeMap<>()` |
| 数组构造器引用 | `int[]::new` | `len -> new int[len]` |

> **复习要点**：方法引用只有在比 Lambda **更短更清晰**时才使用。若 Lambda 包含类型转换或需要组合多个操作，直接使用 Lambda 可能更易读。

---

### 条款44：优先使用标准函数接口

Java 8 `java.util.function` 包提供的六大核心标准接口：

| 接口 | 方法签名 | 说明 |
|------|---------|------|
| `UnaryOperator<T>` | `T apply(T t)` | 一元操作，输入输出同类型 |
| `BinaryOperator<T>` | `T apply(T t1, T t2)` | 二元操作，两个输入一个输出，同类型 |
| `Predicate<T>` | `boolean test(T t)` | 断言，判断条件 |
| `Function<T,R>` | `R apply(T t)` | 函数，T 转 R |
| `Supplier<T>` | `T get()` | 供应器，无输入有输出 |
| `Consumer<T>` | `void accept(T t)` | 消费者，有输入无输出 |

基本类型特化版本（避免自动装箱开销）：

| 类型 | 示例接口 | 方法 |
|------|---------|------|
| int | `IntPredicate` | `boolean test(int value)` |
| long | `LongFunction<R>` | `R apply(long value)` |
| double | `DoubleConsumer` | `void accept(double value)` |

> **复习要点**：
> - 优先使用标准接口，**不要重复造轮子**
> - 基本类型特化版本（如 `IntPredicate`）可避免 `Integer` 自动装箱的开销
> - 仅在标准接口不满足需求时才自定义函数接口，并添加 `@FunctionalInterface` 注解

---

### 条款45：谨慎使用 Stream

#### Stream API 核心操作

| 类型 | 操作 | 说明 |
|------|------|------|
| 中间操作 | `filter(Predicate)` | 按条件过滤元素 |
| 中间操作 | `map(Function)` | 对每个元素进行转换 |
| 中间操作 | `sorted(Comparator)` | 排序 |
| 终止操作 | `forEach(Consumer)` | 遍历消费 |
| 终止操作 | `collect(Collector)` | 收集结果 |
| 终止操作 | `reduce(BinaryOperator)` | 归约聚合 |

#### Stream 的适用场景

**适合使用 Stream**：
- 对元素的**统一转换**（如提取字段、类型转换）
- **过滤**满足特定条件的元素
- **合并**多个数据源
- **搜索**满足条件的元素（`findFirst`、`anyMatch` 等）

**不适合使用 Stream**：
- 需要**修改局部变量**（Lambda 中变量必须是 effectively final）
- 需要 **`return`、`break`、`continue`** 控制流（Stream 中不支持）
- 需要**访问原元素**但在映射后已丢失（需维护逆映射）
- 处理 `char` 值（`Stream<String>` 到字符的转换繁琐）
- 操作有明确的**代码块结构**需要并行执行多种操作

```java
// 过度使用 Stream 的反例（难读）
"Hello world!".chars().filter(Character::isLetter)
    .map(Character::toLowerCase)
    .collect(StringBuilder::new, StringBuilder::appendCodePoint,
             StringBuilder::append)
    .toString();
```

> **复习要点**：Stream 提高了表达能力，但**可读性**仍是首要考量。当 Stream 表达式超过几行时，考虑改用循环或拆分为多个步骤。

---

### 条款46：优先选择 Stream 中无副作用的函数

**纯函数**的定义：结果只依赖输入参数，不依赖任何可变状态，不产生副作用。

```java
// 错误做法：使用副作用（修改外部变量 Map）
Map<String, Long> freq = new HashMap<>();
try (Stream<String> words = new Scanner(file).tokens()) {
    words.forEach(word -> {
        freq.merge(word.toLowerCase(), 1L, Long::sum); // 副作用！
    });
}

// 正确做法：无副作用，使用 Collector
Map<String, Long> freq;
try (Stream<String> words = new Scanner(file).tokens()) {
    freq = words.collect(
        groupingBy(String::toLowerCase, counting()));
}
```

#### 常用 Collector

| Collector | 用途 |
|-----------|------|
| `toList()` | 收集为 List |
| `toSet()` | 收集为 Set |
| `toMap(keyMapper, valueMapper)` | 收集为 Map |
| `toMap(keyMapper, valueMapper, mergeFunction)` | 处理键冲突的 Map |
| `groupingBy(classifier)` | 按分类器分组 |
| `groupingBy(classifier, downstream)` | 分组后二次聚合 |
| `partitioningBy(predicate)` | 按条件分为两组 |
| `counting()` | 计数 |
| `summingInt/Long/Double(mapper)` | 求和 |
| `maxBy(comparator)` / `minBy(comparator)` | 最大/最小值 |
| `joining(delimiter)` | 字符串连接 |

> **复习要点**：
> - `forEach` 应仅用于报告 Stream 计算结果，**不应在 forEach 中修改外部状态**
> - `Collector` 是 Stream 的"收集策略"，将 Stream 元素聚合为结果容器
> - 优先使用内置 Collector，比手动聚合更简洁高效

---

### 条款47：优先选择 Collection 而不是 Stream 作为返回类型

- **Collection**（`List`、`Set` 等）是 `Iterable` 的子类型，同时提供了 `stream()` 方法
- 调用方可以根据需要选择使用**增强 for 循环**或 **Stream API**
- 若返回 `Stream`，调用方无法直接使用 for-each 循环

```java
// 好的做法：返回 Collection
public Collection<V> values() { ... }

// 调用方可选择任一方式
for (V v : obj.values()) { ... }          // for-each
obj.values().stream().filter(...). ...;    // Stream
```

> **复习要点**：如果确定返回值仅用于 Stream 处理，返回 `Stream` 也可以。但对于公共 API，返回 `Collection` 提供更大的灵活性。

---
---

## 第8章 方法

### 条款49：检查参数的有效性

#### 参数检查的必要性

对于公有方法和受保护方法，应在方法体的开头检查参数的有效性：

| 参数类型 | 检查要求 |
|---------|---------|
| 索引值 | 必须在有效范围内（非负，小于数组/集合大小） |
| 对象引用 | 不能为 `null`（除非方法明确允许 null） |
| 范围值 | 必须在合理的数值区间内 |
| 集合/数组 | 非空、元素不重复等 |

**不检查参数的后果**：
- 方法执行过程中**处理失败**，抛出难以定位的异常
- 产生**错误的计算结果**
- **破坏对象的不变性**，使对象处于不一致状态

```java
// 公有方法：显式检查 + 抛出异常
public BigInteger mod(BigInteger m) {
    if (m.signum <= 0)
        throw new ArithmeticException("Modulus <= 0: " + m);
    // ... 执行操作
}

// 使用 Objects.requireNonNull 进行 null 检查
this.strategy = Objects.requireNonNull(strategy, "strategy");
```

#### 非公有方法使用断言

```java
// 私有方法使用 assertion（断言默认关闭，需 -ea 启用）
private static void sort(long a[], int offset, int length) {
    assert a != null;
    assert offset >= 0 && offset <= a.length;
    assert length >= 0 && length <= a.length - offset;
    // ... 执行排序
}
```

> **复习要点**：
> - 公有方法应抛出**具体异常**（如 `IllegalArgumentException`、`IndexOutOfBoundsException`、`NullPointerException`）
> - 断言适用于**开发阶段**验证内部不变量，生产环境可关闭
> - Java 7+ 使用 `Objects.requireNonNull()` 检查 null 参数

---

### 条款50：必要时进行保护性拷贝

#### 问题根源：Date 类是可变的

```java
// 攻击示例：利用 Date 的可变性破坏 Period 的不变性
Date start = new Date();
Date end = new Date();
Period p = new Period(start, end);
end.setYear(78); // 修改了 Period 内部的 end！
```

#### 保护性拷贝的实现

```java
public final class Period {
    private final Date start;
    private final Date end;

    public Period(Date start, Date end) {
        // 保护性拷贝：在检查有效性之前进行（避免 TOCTOU 攻击）
        this.start = new Date(start.getTime());
        this.end   = new Date(end.getTime());

        // 检查参数有效性
        if (this.start.compareTo(this.end) > 0)
            throw new IllegalArgumentException(
                this.start + " after " + this.end);
    }

    public Date start() {
        // 返回拷贝而非原始引用
        return new Date(start.getTime());
    }

    public Date end() {
        return new Date(end.getTime());
    }
}
```

#### 关键原则

1. **保护性拷贝在检查参数有效性之前进行**：防止 **TOCTOU 攻击**（Time-Of-Check-Time-Of-Use，检查时有效但使用时被修改）
2. **不使用 `Date.clone()`**：因为 `Date` 不是 `final` 类，可能被恶意子类覆盖
3. **修改数据访问方法也返回拷贝**：防止调用方通过 getter 获取引用后修改内部状态
4. **长度非零的数组总是可变的**：返回数组时同样需要保护性拷贝

> **复习要点**：
> - 从 Java 8 开始，使用不可变的 `java.time.Instant` 替代 `Date` 可从根本上避免此问题
> - 保护性拷贝有性能开销，仅在**跨信任边界**时使用（如公有 API 参数/返回值）
> - 如果类包内共享且信任调用方，可省略拷贝

---

### 条款51：谨慎设计方法签名

#### 原则总结

| 原则 | 说明 |
|------|------|
| **谨慎选择方法名称** | 遵循命名约定，选择易理解、与包内其他名称一致的名字 |
| **不要过度提供便利方法** | 类的方法太多会使学习、使用、维护困难；每个方法应有明确的用途 |
| **避免过长的参数列表** | 四个或更少参数；超过时应拆分方法或使用辅助类 |
| **参数优先使用接口而非类** | 如使用 `Map` 而非 `HashMap`，使方法更通用 |
| **Boolean 参数优先使用两个元素的枚举** | 如 `Thermometer.newInstance(TemperatureScale.CELSIUS)` 比 `newInstance(true)` 可读性更好 |

#### 缩短参数列表的技巧

- **分解方法**：将大方法拆分为多个小方法
- **创建参数对象**：将相关参数封装为辅助类（如 `Point`、`DateRange`）
- **从对象中构建**：采用 Builder 模式

---

### 条款52：明智地使用重载

#### 重载 vs 覆盖

| 特性 | 重载（Overloading） | 覆盖（Overriding） |
|------|-------------------|-------------------|
| 方法选择时机 | **编译时**静态决定 | **运行时**动态决定 |
| 方法签名要求 | 参数类型/数量不同 | 完全相同 |
| 多态性 | 不支持 | 支持 |

#### 重载的危险性

```java
// 问题示例：自动装箱导致重载选择困惑
public class SetList {
    public static void main(String[] args) {
        Set<Integer> set = new TreeSet<>();
        List<Integer> list = new ArrayList<>();

        for (int i = -3; i < 3; i++) {
            set.add(i);
            list.add(i);
        }

        for (int i = 0; i < 3; i++) {
            set.remove(i);      // 调用 remove(Object) -> 按值移除元素
            list.remove(i);     // 调用 remove(int index) -> 按索引移除！
        }

        System.out.println(set + " " + list);
        // 输出：[-3, -2, -1] [-2, 0, 2]  // 结果完全不同！
    }
}
```

#### 避免重载陷阱的准则

1. **不要写出两个具有相同参数数目的重载方法**（尤其是参数类型存在自动转换时）
2. 如果参数类型完全不同（如 `int` 和 `String`），重载是安全的
3. 如果参数是**相同接口**的不同实现，重载可能导致混乱
4. 可以使用**不同方法名**代替重载（如 `writeInt(int)`、`writeLong(long)`）

> **复习要点**：`List.remove(int)` 按索引移除，`List.remove(Object)` 按值移除——这是 Java API 中重载设计不当的经典案例。

---

### 条款53：明智地使用可变参数

#### 需要 1 个或多个参数时的正确做法

```java
// 错误做法：参数可能为空，运行时才能发现
static int min(int... args) {
    if (args.length == 0)
        throw new IllegalArgumentException("Too few arguments");
    int min = args[0];
    for (int i = 1; i < args.length; i++)
        if (args[i] < min) min = args[i];
    return min;
}

// 正确做法：至少需要一个参数（编译期即可保证）
static int min(int firstArg, int... remainingArgs) {
    int min = firstArg;
    for (int arg : remainingArgs)
        if (arg < min) min = arg;
    return min;
}
```

#### 性能优化：为常用参数数量提供专门重载

```java
// EnumSet.of() 的设计：为 1~5 个参数提供专门重载
public static <E extends Enum<E>> EnumSet<E> of(E e) { ... }
public static <E extends Enum<E>> EnumSet<E> of(E e1, E e2) { ... }
public static <E extends Enum<E>> EnumSet<E> of(E e1, E e2, E e3) { ... }
public static <E extends Enum<E>> EnumSet<E> of(E e1, E e2, E e3, E e4) { ... }
public static <E extends Enum<E>> EnumSet<E> of(E e1, E e2, E e3, E e4, E e5) { ... }
public static <E extends Enum<E>> EnumSet<E> of(E first, E... rest) { ... }
```

> **复习要点**：
> - 可变参数在内部创建数组，每次调用都有**数组分配和初始化开销**
> - 对于性能敏感且频繁调用的方法，为常用参数数量提供**专门重载**可消除大部分可变参数开销
> - 95% 的场景只需要 0~3 个参数，为这些情况提供专门版本

---

### 条款54：返回零长度的数组或集合，而不是 null

返回 `null` 的弊端：
- 调用方必须编写**特殊的 null 检查代码**
- 遗漏检查会导致 `NullPointerException`
- 增加代码复杂度和出错概率

**正确做法**：返回**空数组**或**空集合**。

```java
// 返回空数组
private static final Cheese[] EMPTY_CHEESE_ARRAY = new Cheese[0];

public Cheese[] getCheeses() {
    return cheesesInStock.toArray(EMPTY_CHEESE_ARRAY);
}

// 返回空集合
public List<Cheese> getCheeses() {
    return cheesesInStock.isEmpty()
        ? Collections.emptyList()
        : new ArrayList<>(cheesesInStock);
}
```

> **复习要点**：
> - `Collections.emptyList()`、`emptySet()`、`emptyMap()` 返回不可变的单例空集合，无额外分配开销
> - 返回数组时使用 `toArray(EMPTY_ARRAY)` 模式（传入空数组，由 toArray 按需分配）
> - **不要为了提高性能而返回 null**——返回空集合的性能影响通常微乎其微

---

### 条款55：明智地返回 Optional

#### 方法无法返回值时的三种选择

| 方案 | 使用场景 |
|------|---------|
| **抛出异常** | 无法返回值是**异常情况** |
| **返回 null** | 调用方必须特殊处理（不推荐） |
| **返回 `Optional<T>`** | 可能没有返回值是**正常情况** |

#### Optional 的核心方法

| 方法 | 说明 |
|------|------|
| `Optional.of(value)` | 创建包含非 null 值的 Optional，值为 null 抛 NPE |
| `Optional.ofNullable(value)` | 创建 Optional，允许 null（转为 empty） |
| `Optional.empty()` | 创建空的 Optional |
| `isPresent()` | 判断是否有值 |
| `get()` | 获取值（无值时抛 `NoSuchElementException`） |
| `orElse(defaultValue)` | 有值返回值，无值返回默认值 |
| `orElseThrow(exceptionSupplier)` | 有值返回值，无值抛指定异常 |
| `ifPresent(consumer)` | 有值时执行操作 |

```java
// 使用 Optional 的方法签名
public static <E extends Comparable<E>> Optional<E> max(Collection<E> c) {
    if (c.isEmpty())
        return Optional.empty();
    E result = null;
    for (E e : c)
        if (result == null || e.compareTo(result) > 0)
            result = Objects.requireNonNull(e);
    return Optional.of(result);
}

// 调用方使用
Optional<String> max = max(words);
max.ifPresent(System.out::println);           // 有值时打印
String result = max.orElse("default");        // 提供默认值
String result = max.orElseThrow(() -> new IllegalStateException("empty"));
```

> **复习要点**：
> - `Optional` 设计目标是作为**返回值类型**，不推荐用作字段或方法参数
> - 永远不要用 `Optional.isPresent()` + `Optional.get()` 替代 `if-else`，这是反模式
> - 基本类型有专门的 `OptionalInt`、`OptionalLong`、`OptionalDouble`，避免装箱开销
> - Stream 的终止操作（如 `findFirst`、`max`、`min`）天然返回 Optional

---

## 复习速查表

| 章节 | 条款 | 核心要点 |
|------|------|---------|
| 第6章 | 34 | 用 `enum` 代替 int/string 常量 |
| 第6章 | 35 | 用实例域代替 `ordinal()` |
| 第6章 | 36 | 用 `EnumSet` 代替位域 |
| 第6章 | 37 | 用 `EnumMap` 代替序数索引 |
| 第6章 | 38 | 用接口模拟可扩展的枚举 |
| 第6章 | 39 | 注解优先于命名模式 |
| 第7章 | 42 | Lambda 优先于匿名类 |
| 第7章 | 43 | 方法引用优先于 Lambda |
| 第7章 | 44 | 优先使用标准函数接口 |
| 第7章 | 45 | 谨慎使用 Stream |
| 第7章 | 46 | Stream 中优先使用无副作用的函数 |
| 第7章 | 47 | 优先返回 Collection 而非 Stream |
| 第8章 | 49 | 检查参数的有效性 |
| 第8章 | 50 | 必要时进行保护性拷贝 |
| 第8章 | 51 | 谨慎设计方法签名 |
| 第8章 | 52 | 明智地使用重载 |
| 第8章 | 53 | 明智地使用可变参数 |
| 第8章 | 54 | 返回空数组/集合而非 null |
| 第8章 | 55 | 明智地返回 Optional |
