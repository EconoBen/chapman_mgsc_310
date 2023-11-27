# chapman_mgsc_310
This repo and its contents are for Chapman University students of MGSC 310: Statistical Models for Business Analytics (Introduction to Machine Learning)


### Guide to Class Lesson
1. docker pull qdrant/qdrant
2. run docker in tmux so as to ensure it's still running
   - `tmux new-se
ssion -s "class"`
3. 
   - [WebUI](http://localhost:6333/dashboard)
   - [pythonAPI](localhost:6333)
4. `docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant`
5.    