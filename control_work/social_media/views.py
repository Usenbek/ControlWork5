from .serializers import PostListSerializer, CommentSerializer, PostDetailSerializer, CommentDetailSerializer
from .models import Post, Comment
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework.authentication import SessionAuthentication


# Create your views here.


#для каждого запроса кроме чтения данных нужно быть авторизованным


#Лист постов и создание
class PostListAPIView(ListCreateAPIView):
      queryset = Post.objects.all()
      serializer_class = PostListSerializer
      permission_classes = [IsAuthenticatedOrReadOnly]
      authentication_classes = [SessionAuthentication]

      def perform_create(self, serializer):
            serializer.save(author=self.request.user)

#Подробная информация про определенный пост и его редактирование для автора поста(по id)
class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
      queryset = Post.objects.all()
      lookup_field = 'id'
      serializer_class = PostDetailSerializer
      permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

      def perform_create(self, serializer):
        post_id = self.kwargs['id']
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)

#Просмотр комментариев под постом и добавления комментария 
class PostCommentListAPIView(ListCreateAPIView):
      serializer_class = CommentSerializer
      permission_classes = [IsAuthenticatedOrReadOnly]
      def get_queryset(self):
            post_id = self.kwargs['id']
            return Comment.objects.filter(post_id=post_id)
      
      def perform_create(self, serializer):
        post_id = self.kwargs['id']
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)

#просмотр детального комментария для редактирования и удаления комментария для автора комментария
class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


      


