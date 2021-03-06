"""initial migration

Revision ID: f1030c254ab4
Revises: ad0827a1c9d7
Create Date: 2016-09-11 00:41:14.478000

"""

# revision identifiers, used by Alembic.
revision = 'f1030c254ab4'
down_revision = 'ad0827a1c9d7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('body_html', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_timestamp'), 'posts', ['timestamp'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('body_html', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_timestamp'), 'comments', ['timestamp'], unique=False)
    op.add_column(u'roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column(u'roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.add_column(u'users', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column(u'users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    op.add_column(u'users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    op.add_column(u'users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column(u'users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column(u'users', sa.Column('location', sa.String(length=64), nullable=True))
    op.add_column(u'users', sa.Column('member_since', sa.DateTime(), nullable=True))
    op.add_column(u'users', sa.Column('name', sa.String(length=64), nullable=True))
    op.add_column(u'users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column(u'users', 'password_hash')
    op.drop_column(u'users', 'name')
    op.drop_column(u'users', 'member_since')
    op.drop_column(u'users', 'location')
    op.drop_column(u'users', 'last_seen')
    op.drop_column(u'users', 'email')
    op.drop_column(u'users', 'confirmed')
    op.drop_column(u'users', 'avatar_hash')
    op.drop_column(u'users', 'about_me')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column(u'roles', 'permissions')
    op.drop_column(u'roles', 'default')
    op.drop_index(op.f('ix_comments_timestamp'), table_name='comments')
    op.drop_table('comments')
    op.drop_index(op.f('ix_posts_timestamp'), table_name='posts')
    op.drop_table('posts')
    op.drop_table('follows')
    ### end Alembic commands ###
