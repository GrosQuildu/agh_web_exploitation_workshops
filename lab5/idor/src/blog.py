from app import app, db
from app.models import User, Post
from config import ADMIN_PASS, ADMIN_PATH, FLAG_IDOR, FLAG_IDOR_SLUG, MAGIC_FLAG, MAGIC_FLAG_SLUG


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

def seed():
    admin = User.query.filter_by(username="admin").first()
    if not admin:
        admin = User(username="admin")
        admin.set_password(ADMIN_PASS)
        db.session.add(admin)
        db.session.commit()

    random_user = User.query.filter_by(username="random_user").first()
    if not random_user:
        random_user = User(username="random_user")
        random_user.set_password("1q2w3e4r5t6y7u8i9o0p-[=]")
        db.session.add(random_user)
        db.session.commit()

    if not Post.query.filter_by(title="FLAG_IDOR").first():
        post = Post(title="FLAG_IDOR", content=FLAG_IDOR)
        post.update_slug_static(FLAG_IDOR_SLUG)
        admin.posts.append(post)
        db.session.commit()

    if not Post.query.filter_by(title="MAGIC_SLUG").first():
        post = Post(title="MAGIC_SLUG", content=MAGIC_FLAG)
        post.update_slug_hash(MAGIC_FLAG_SLUG)
        admin.posts.append(post)
        db.session.commit()

    if not Post.query.filter_by(title="Serious one").first():
        post = Post(title="Serious one", content="You really thought that?")
        post.update_slug_static("1")
        random_user.posts.append(post)
        db.session.commit()

    if not Post.query.filter_by(title="The data and the bases").first():
        post = Post(title="The data and the bases", content="Just give me 3.0")
        post.update_slug_static("2")
        random_user.posts.append(post)
        db.session.commit()

    if not Post.query.filter_by(title="The data and the bases 2").first():
        post = Post(title="The data and the bases 2", content="Okey, I can retake it")
        post.update_slug_static("3")
        random_user.posts.append(post)
        db.session.commit()

    if not Post.query.filter_by(title="The data and the bases: Prequel").first():
        post = Post(title="The data and the bases: Prequel", content="This year I will make every assignment before the last day of the deadline")
        post.update_slug_static("4")
        random_user.posts.append(post)
        db.session.commit()

    if not Post.query.filter_by(title="The Dziekanka").first():
        post = Post(title="The Dziekanka", content="Automaty jednak nie takie fajne")
        post.update_slug_static("5")
        random_user.posts.append(post)
        db.session.commit()

    if not Post.query.filter_by(title="Creativity").first():
        post = Post(title="Creativity", content="Nothing comes to my mind, so here You go, some wiki theory: A cryptographic hash function (CHF) is a hash function that is suitable for use in cryptography. It is a mathematical algorithm that maps data of arbitrary size (often called the 'message') to a bit string of a fixed size (the 'hash value', 'hash', or 'message digest') and is a one-way function, that is, a function which is practically infeasible to invert. Ideally, the only way to find a message that produces a given hash is to attempt a brute-force search of possible inputs to see if they produce a match, or use a rainbow table of matched hashes. Cryptographic hash functions are a basic tool of modern cryptography.")
        post.update_slug_static("6")
        random_user.posts.append(post)
        db.session.commit()
    
    if not Post.query.filter_by(title="Read this after creativity").first():
        post = Post(title="Read this after creativity", content="So this was hash definition, there is another one: Hashish, or hash, is a drug made from the resin of the cannabis plant. It is consumed by smoking a small piece, typically in a pipe, bong, vaporizer or joint, or via oral ingestion (after decarboxylation). As pure hashish will not burn if rolled alone in a joint, it is typically mixed with herbal cannabis, tobacco or another type of herb for this method of consumption. Depending on region or country, multiple synonyms and alternative names exist.")
        post.update_slug_static("7")
        random_user.posts.append(post)
        db.session.commit()

    if not Post.query.filter_by(title="How many moreeeeeeeee").first():
        post = Post(title="How many moreeeeeeeee", content="Over 9000")
        post.update_slug_static("9")
        random_user.posts.append(post)
        db.session.commit()

    if not Post.query.filter_by(title="Near the end").first():
        post = Post(title="Near the end", content="Nice :3")
        post.update_slug_static("10")
        random_user.posts.append(post)
        db.session.commit()

    if not Post.query.filter_by(title="The last one").first():
        post = Post(title="The last one", content="The last one jedi")
        post.update_slug_static("11")
        random_user.posts.append(post)
        db.session.commit()


if __name__ == '__main__':
    seed()
    app.run(debug=False, host='0.0.0.0')