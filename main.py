import argparse
import training
import datasets


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CIFAR10 image classification')
    parser = argparse.ArgumentParser(description='CIFAR10 image classification')
    parser.add_argument('--batch_size', default=128, type=int, help='batch size')
    parser.add_argument('--epoch', default=101, type=int, help='training epoch')
    parser.add_argument('--lr', default=1e-3, type=float, help='learning rate')
    parser.add_argument('--model_name', default='resnet18', type=str, help='model name')
    parser.add_argument('--train', default='train', type=str, help='train and eval')
    args = parser.parse_args()
    print(args)

    # 데이터 불러오기
    train_generator, test_generator = datasets.dataloader(args.batch_size)
    print("데이터를 잘 준비했습니다.")

    # 모델 불러오기 및 학습하기
    if args.train == 'train':
        learning = training.train_model(train_generator, args.epoch)
    else:
        train_acc = learning.eval_model(trainloader)
        test_acc = learning.eval_model(testloader)
        print(f' Train Accuracy: {train_acc}, Test Accuracy: {test_acc}')
