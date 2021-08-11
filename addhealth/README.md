# Social Networks from the *National Longitudinal Study of Adolescent to Adult Health*

The following description is based on [Linton Freeman's data website](https://web.archive.org/web/20210115130726/http://moreno.ss.uci.edu/data.html#adhealth), and some text is reproduced exactly. The data presented here encode the networks as platform and language agnostic [GraphML](https://en.wikipedia.org/wiki/GraphML) datasets, and attributes have been coded literally (e.g. the sex attribute is `female` instead of `2`). Most data were obtained from Freeman's website, but the attributes for community 48 are missing, and they were obtained from [Zack Alquists' network data repository](https://github.com/zalmquist/networkdata). Neither dataset is sufficient because Alquists' dataset contains some values in the `race` attribute that are not permissible in community 35.

## Dataset description

The dataset comprises friendship choices made by students from 84 communities. Each community contains either one or two junior high or high schools. The numbers of students in each community vary between 25 and 2587. In each case, the data include friendship choices and various individual characteristics (except for community 48 for which individual attributes are missing).

The ADD HEALTH data are constructed from the in-school questionnaire; 90,118 students representing 84 communities took this survey in 1994-95. Some communities had only one school; others had two. Where there are two schools in a community students from one school were allowed to name friends in the other, the "sister school."

Each student was given a paper-and-pencil questionnaire and a copy of a roster listing every student in the school and, if the community had two schools, the student was provided with the roster of the "sister" school. The name generator asked about five male and five female friends separately. The question was, "List your closest (male/female) friends. List your best (male/female) friend first, then your next best friend, and so on." For each friend named, the student was asked to check off whether he/she participated in any of five activities with the friend. These activities were:

1. you went to (his/her) house in the last seven days.
2. you met (him/her) after school to hang out or go somewhere in the last seven days.
3. you spent time with (him/her) last weekend.
4. you talked with (him/her) about a problem in the last seven days.
5. you talked with (him/her) on the telephone in the last seven days.

These activities were summed to create a valued network. Ties range in value from 1, meaning the student nominated the friend but reported no activities, to 6, meaning the student nominated the friend and reported participating in all five activities with the friend.

Because nominations to friends in the sister school were allowed, the networks here are reported at the community level. When two schools were present in a community the data file includes a node-level indicator for school code, so one can easily extract choices from the separate schools.

For the raw data, the friendship choices are recorded in the COMM files. And the COMM_ATT files include the sex, race, grade in school and, in communities that have two schools, the school code. Sex was coded 1=male, 2=female, 0=unreported. Race was coded 1=white, 2=black, 3=hispanic, 4=asian, 5=mixed/other, 0=unreported. Grade was recorded as a number between 7 and 12 with 0=unreported. And school codes are 0 and 1 when two schools were in a single community.
